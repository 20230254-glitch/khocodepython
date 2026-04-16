import tkinter as tk
from tkinter import ttk, messagebox
import nhansu_service as sv
import database  

root = tk.Tk()
root.title("Quản lý nhân sự")
root.geometry("1000x600")
root.configure(bg="#f0f2f5")

# ===== STYLE =====
style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=25,
                fieldbackground="white")

style.configure("Treeview.Heading",
                font=("Arial", 10, "bold"))

# ===== TITLE =====
title = tk.Label(root, text="HỆ THỐNG QUẢN LÝ NHÂN SỰ",
                 font=("Arial", 18, "bold"),
                 bg="#f0f2f5", fg="#333")
title.pack(pady=10)

# ===== FRAME CHÍNH =====
main_frame = tk.Frame(root, bg="#f0f2f5")
main_frame.pack(fill="both", expand=True, padx=10)

# ===== FRAME INPUT =====
frame_input = tk.LabelFrame(main_frame, text="Thông tin nhân sự",
                            font=("Arial", 10, "bold"),
                            bg="#f0f2f5", padx=10, pady=10)
frame_input.pack(side="left", fill="y", padx=10)

# Label + Entry
def create_row(label, row):
    tk.Label(frame_input, text=label, bg="#f0f2f5").grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(frame_input, width=25)
    entry.grid(row=row, column=1, pady=5)
    return entry

txt_cccd = create_row("CCCD:", 0)
txt_hoten = create_row("Họ tên:", 1)
txt_ngaysinh = create_row("Ngày sinh:", 2)

tk.Label(frame_input, text="Giới tính:", bg="#f0f2f5").grid(row=3, column=0, sticky="w", pady=5)
gioitinh = ttk.Combobox(frame_input, values=["Nam", "Nữ"], width=22)
gioitinh.grid(row=3, column=1, pady=5)

txt_diachi = create_row("Địa chỉ:", 4)

# ===== BUTTON =====
btn_frame = tk.Frame(frame_input, bg="#f0f2f5")
btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

def create_button(text, cmd, color):
    return tk.Button(btn_frame, text=text, command=cmd,
                     bg=color, fg="white", width=10, relief="flat")

btnThem = create_button("Thêm", lambda: them(), "#28a745")
btnSua = create_button("Sửa", lambda: sua(), "#007bff")
btnXoa = create_button("Xóa", lambda: xoa(), "#dc3545")
btnTim = create_button("Tìm", lambda: tim(), "#6c757d")

btnThem.grid(row=0, column=0, padx=5)
btnSua.grid(row=0, column=1, padx=5)
btnXoa.grid(row=0, column=2, padx=5)
btnTim.grid(row=0, column=3, padx=5)

# ===== FRAME TABLE =====
frame_table = tk.Frame(main_frame)
frame_table.pack(side="right", fill="both", expand=True)

columns = ("cccd", "hoten", "ngaysinh", "gioitinh", "diachi")

tree = ttk.Treeview(frame_table, columns=columns, show="headings")

# đặt tên cột đẹp
tree.heading("cccd", text="CCCD")
tree.heading("hoten", text="Họ tên")
tree.heading("ngaysinh", text="Ngày sinh")
tree.heading("gioitinh", text="Giới tính")
tree.heading("diachi", text="Địa chỉ")

# chỉnh độ rộng
tree.column("cccd", width=120)
tree.column("hoten", width=150)
tree.column("ngaysinh", width=100)
tree.column("gioitinh", width=80)
tree.column("diachi", width=200)

tree.pack(fill="both", expand=True)

# Scrollbar
scroll = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

# ===== FUNCTION =====
def load_data(data=None):
    for row in tree.get_children():
        tree.delete(row)

    if data is None:
        data = sv.get_all()

    for row in data:
        tree.insert("", "end", values=row)

def them():
    try:
        sv.them((
            txt_cccd.get(),
            txt_hoten.get(),
            txt_ngaysinh.get(),
            gioitinh.get(),
            txt_diachi.get()
        ))
        load_data()
    except:
        messagebox.showerror("Lỗi", "CCCD đã tồn tại!")

def sua():
    sv.sua((
        txt_cccd.get(),
        txt_hoten.get(),
        txt_ngaysinh.get(),
        gioitinh.get(),
        txt_diachi.get()
    ))
    load_data()

def xoa():
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa?"):
        sv.xoa(txt_cccd.get())
        load_data()

def tim():
    data = sv.timkiem(txt_hoten.get())
    load_data(data)

def select_item(event):
    selected = tree.item(tree.focus())["values"]
    if selected:
        txt_cccd.delete(0, tk.END)
        txt_cccd.insert(0, selected[0])

        txt_hoten.delete(0, tk.END)
        txt_hoten.insert(0, selected[1])

        txt_ngaysinh.delete(0, tk.END)
        txt_ngaysinh.insert(0, selected[2])

        gioitinh.set(selected[3])

        txt_diachi.delete(0, tk.END)
        txt_diachi.insert(0, selected[4])

tree.bind("<<TreeviewSelect>>", select_item)

load_data()
root.mainloop()