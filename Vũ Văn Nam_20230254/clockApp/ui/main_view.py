import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from lunardate import LunarDate
import threading, time
from datetime import datetime
import pytz

# ================= MODERN UI COLORS =================
BG = "#0f172a"      
CARD = "#1e293b"    
ACCENT = "#38bdf8"   
TEXT = "#e2e8f0"      
SUBTEXT = "#94a3b8"   
BTN = "#22c55e"      
BTN_DANGER = "#ef4444"

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Clock Pro")
        self.root.geometry("950x600")
        self.root.configure(bg=BG)

        # ===== STYLE =====
        style = ttk.Style()
        style.theme_use("clam")

        # ===== HEADER =====
        header = tk.Frame(root, bg=BG)
        header.pack(fill="x", pady=10)

        self.time_label = tk.Label(header, text="--:--:--",
                                   font=("Segoe UI", 34, "bold"),
                                   fg=ACCENT, bg=BG)
        self.time_label.pack()

        # ===== MAIN LAYOUT =====
        main = tk.Frame(root, bg=BG)
        main.pack(fill="both", expand=True, padx=20, pady=10)

        # ===== LEFT PANEL =====
        left = tk.Frame(main, bg=CARD)
        left.place(relwidth=0.38, relheight=1)

        tk.Label(left, text=" Múi giờ", fg=TEXT, bg=CARD,
                 font=("Segoe UI", 14, "bold")).pack(pady=10)

        self.timezone_var = tk.StringVar()
        self.cb = ttk.Combobox(left, state="readonly",
                               values=[
                                   "Asia/Ho_Chi_Minh",
                                   "UTC",
                                   "US/Eastern",
                                   "Europe/London",
                                   "Asia/Tokyo"
                               ], textvariable=self.timezone_var)
        self.cb.current(0)
        self.cb.pack(pady=5)

        # ===== OPTION =====
        self.show_seconds = tk.BooleanVar(value=True)
        tk.Checkbutton(left, text="Hiển thị giây",
                       variable=self.show_seconds,
                       fg=SUBTEXT, bg=CARD,
                       activebackground=CARD).pack(pady=5)

        # ===== RIGHT PANEL =====
        right = tk.Frame(main, bg=CARD)
        right.place(relx=0.4, relwidth=0.6, relheight=1)

        tk.Label(right, text=" Lịch & Sự kiện",
                 fg=TEXT, bg=CARD,
                 font=("Segoe UI", 14, "bold")).pack(pady=10)

        tk.Label(right, text="Loại lịch",
                 fg=SUBTEXT, bg=CARD,
                 font=("Segoe UI", 10)).pack(pady=5)

        self.calendar_type = ttk.Combobox(
            right,
            values=["Dương lịch", "Âm lịch"],
            state="readonly"
        )
        self.calendar_type.current(0)
        self.calendar_type.pack(pady=5)

        self.cal = Calendar(right, selectmode="day")
        self.cal.pack(pady=5)

        # ===== INPUT =====
        self.entry = tk.Entry(right, font=("Segoe UI", 11))
        self.entry.insert(0, "Nội dung | HH:MM")
        self.entry.pack(pady=5, ipadx=5, ipady=3)

        btn_frame = tk.Frame(right, bg=CARD)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text=" Thêm",
                  bg=BTN, fg="white",
                  font=("Segoe UI", 10, "bold"),
                  command=self.add_event).pack(side="left", padx=5)

        tk.Button(btn_frame, text=" Xóa",
                  bg=BTN_DANGER, fg="white",
                  font=("Segoe UI", 10, "bold"),
                  command=self.delete_event).pack(side="left", padx=5)

        # ===== LIST =====
        self.listbox = tk.Listbox(right,
                                 bg="#020617",
                                 fg=TEXT,
                                 font=("Segoe UI", 11),
                                 selectbackground=ACCENT)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.events = []

        # ===== THREAD =====
        threading.Thread(target=self.update_time, daemon=True).start()
        threading.Thread(target=self.check_reminder, daemon=True).start()

    # ===== TIME =====
    def update_time(self):
        while True:
            try:
                tz = pytz.timezone(self.timezone_var.get())
                now = datetime.now(tz)
            except:
                now = datetime.now()

            if self.show_seconds.get():
                fmt = "%H:%M:%S - %d/%m/%Y"
            else:
                fmt = "%H:%M - %d/%m/%Y"

            self.time_label.config(text=now.strftime(fmt))
            time.sleep(1)

    # ===== EVENT =====
    def add_event(self):
        text = self.entry.get()
        date = self.cal.get_date()

        if not text or "|" not in text:
            messagebox.showwarning("Lỗi", "Nhập dạng: nội dung | HH:MM")
            return

        content, time_str = text.split("|")
        content = content.strip()
        time_str = time_str.strip()

        try:
            hour, minute = map(int, time_str.split(":"))
            month, day, year = map(int, date.split("/"))
            year += 2000

            event_time = datetime(year, month, day, hour, minute)
        except:
            messagebox.showerror("Lỗi", "Sai định dạng giờ")
            return

        cal_type = self.calendar_type.get()

        if cal_type == "Âm lịch":
            lunar_date = self.solar_to_lunar(date)
            display_date = f"{lunar_date} (Âm)"
        else:
            display_date = date

        self.events.append((event_time, content))
        self.listbox.insert(tk.END, f"{display_date} {time_str} - {content}")
        self.entry.delete(0, tk.END)

    def delete_event(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected[0])

    def solar_to_lunar(self, date_str):
        try:
            month, day, year = map(int, date_str.split("/"))
            year += 2000
            lunar = LunarDate.fromSolarDate(year, month, day)
            return f"{lunar.day}/{lunar.month}/{lunar.year}"
        except:
            return "Lỗi chuyển đổi"

    # ===== REMINDER =====
    def check_reminder(self):
        while True:
            now = datetime.now()

            for event in self.events[:]:
                event_time, content = event

                if abs((event_time - now).total_seconds()) < 60:
                    messagebox.showinfo(" Nhắc lịch", content)
                    self.events.remove(event)

            time.sleep(30)

# ===== RUN =====
if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()