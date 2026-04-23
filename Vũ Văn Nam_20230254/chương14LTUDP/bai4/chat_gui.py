import socket
import threading
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

# ===== UI MESSAGE =====
def create_bubble(parent, msg, is_me):
    frame = tk.Frame(parent, bg="#f0f0f0")

    time = datetime.now().strftime("%H:%M")

    bubble = tk.Label(
        frame,
        text=f"{msg}\n{time}",
        bg="#4CAF50" if is_me else "#e0e0e0",
        fg="white" if is_me else "black",
        padx=10,
        pady=5,
        wraplength=250,
        justify="left"
    )

    if is_me:
        bubble.pack(anchor="e", padx=10, pady=5)
    else:
        bubble.pack(anchor="w", padx=10, pady=5)

    frame.pack(fill="both", expand=True)

# ===== MAIN WINDOW =====
window = tk.Tk()
window.title("💬 Chat TCP Pro")
window.geometry("500x600")
window.configure(bg="#f0f0f0")

# ===== HEADER =====
header = tk.Label(window, text="Chat App", bg="#2196F3", fg="white", font=("Arial", 14))
header.pack(fill=tk.X)

# ===== CHAT AREA =====
chat_frame = tk.Frame(window, bg="#f0f0f0")
chat_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(chat_frame, bg="#f0f0f0")
scrollbar = tk.Scrollbar(chat_frame, command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ===== INPUT =====
bottom = tk.Frame(window, bg="#ddd")
bottom.pack(fill=tk.X)

entry = tk.Entry(bottom, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

# ===== SOCKET =====
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mode = simpledialog.askstring("Mode", "server / client:")
mode = mode.strip().lower()
name = simpledialog.askstring("Tên", "Nhập tên của bạn:")

if mode == "server":
    sock.bind(('0.0.0.0', 8098))
    sock.listen(1)
    create_bubble(scrollable_frame, "Đang chờ client...", False)
    conn, addr = sock.accept()
    create_bubble(scrollable_frame, f"Đã kết nối {addr}", False)

    def send_msg(msg):
        conn.send(msg.encode())

    def receive():
        while True:
            try:
                data = conn.recv(1024)
                if data:
                    create_bubble(scrollable_frame, data.decode(), False)
            except:
                break

elif mode == "client":
    ip = simpledialog.askstring("IP", "Nhập IP server:")
    sock.connect((ip, 8098))
    create_bubble(scrollable_frame, f"Kết nối tới {ip}", False)

else:
    print("Sai mode! Chỉ nhập server hoặc client")
    exit()
    
    def send_msg(msg):
        sock.send(msg.encode())

    def receive():
        while True:
            try:
                data = sock.recv(1024)
                if data:
                    create_bubble(scrollable_frame, data.decode(), False)
            except:
                break

# ===== SEND =====
def send(event=None):
    msg = entry.get()
    if msg:
        full_msg = f"{name}: {msg}"
        send_msg(full_msg)
        create_bubble(scrollable_frame, full_msg, True)
        entry.delete(0, tk.END)

entry.bind("<Return>", send)

btn_send = tk.Button(bottom, text="Gửi", bg="#4CAF50", fg="white", command=send)
btn_send.pack(side=tk.RIGHT, padx=5)

btn_emoji = tk.Button(bottom, text="😀", command=lambda: entry.insert(tk.END, "😀"))
btn_emoji.pack(side=tk.RIGHT)

# ===== THREAD =====
threading.Thread(target=receive, daemon=True).start()

window.mainloop()