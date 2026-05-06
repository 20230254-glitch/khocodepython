import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Monitoring System")
        self.root.geometry("900x700")
        self.root.configure(bg="#eef2f7")

        style = ttk.Style()
        style.theme_use("clam")

        self.build_ui()

    def build_ui(self):
        # ===== MAIN CONTAINER =====
        container = tk.Frame(self.root, bg="#eef2f7")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # ===== TITLE =====
        title = tk.Label(container, text="Dashboard Theo Dõi Sức Khỏe",
                         font=("Arial", 20, "bold"),
                         bg="#eef2f7", fg="#2c3e50")
        title.pack(pady=10)

        # ===== TOP: FORM + STATS =====
        top_frame = tk.Frame(container, bg="#eef2f7")
        top_frame.pack(fill="x")

        # ===== FORM CARD =====
        form_card = tk.Frame(top_frame, bg="white", bd=1, relief="solid")
        form_card.pack(side="left", fill="both", expand=True, padx=5)

        tk.Label(form_card, text="Nhập dữ liệu",
                 font=("Arial", 14, "bold"),
                 bg="white").grid(row=0, columnspan=2, pady=10)

        self.weight_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.heart_var = tk.StringVar()
        self.co2_var = tk.StringVar()

        self.create_input(form_card, "Cân nặng (kg):", self.weight_var, 1)
        self.create_input(form_card, "Chiều cao (cm):", self.height_var, 2)
        self.create_input(form_card, "Nhịp tim:", self.heart_var, 3)
        self.create_input(form_card, "CO2:", self.co2_var, 4)

        self.btn = ttk.Button(form_card, text="Phân tích",
                              command=self.on_submit)
        self.btn.grid(row=5, columnspan=2, pady=10)

        self.result_label = tk.Label(form_card, text="", bg="white",
                                     fg="green", font=("Arial", 11))
        self.result_label.grid(row=6, columnspan=2, pady=5)

        # ===== STATS CARD =====
        stats_card = tk.Frame(top_frame, bg="white", bd=1, relief="solid")
        stats_card.pack(side="right", fill="both", expand=True, padx=5)

        tk.Label(stats_card, text="Thống kê",
                 font=("Arial", 14, "bold"),
                 bg="white").pack(pady=10)

        self.stats_label = tk.Label(stats_card, text="", bg="white",
                                   font=("Arial", 11), fg="#2c3e50", justify="left")
        self.stats_label.pack(pady=10)

        # ===== TABLE =====
        table_card = tk.Frame(container, bg="white", bd=1, relief="solid")
        table_card.pack(fill="both", expand=True, pady=10)

        tk.Label(table_card, text="Lịch sử đo",
                 font=("Arial", 14, "bold"),
                 bg="white").pack(pady=5)

        columns = ("weight", "height", "bmi", "heart", "co2")
        self.tree = ttk.Treeview(table_card, columns=columns, show="headings", height=8)

        self.tree.heading("weight", text="Cân nặng")
        self.tree.heading("height", text="Chiều cao")
        self.tree.heading("bmi", text="BMI")
        self.tree.heading("heart", text="Nhịp tim")
        self.tree.heading("co2", text="CO2")

        for col in columns:
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # ===== CHART =====
        chart_card = tk.Frame(container, bg="white", bd=1, relief="solid")
        chart_card.pack(fill="both", expand=True)

        tk.Label(chart_card, text="Biểu đồ sức khỏe",
                 font=("Arial", 14, "bold"),
                 bg="white").pack(pady=5)

        self.fig, self.ax = plt.subplots(figsize=(6, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_card)
        self.canvas.get_tk_widget().pack()

    def create_input(self, frame, text, var, row):
        tk.Label(frame, text=text, bg="white").grid(row=row, column=0, padx=10, pady=5)
        ttk.Entry(frame, textvariable=var).grid(row=row, column=1, padx=10, pady=5)

    def set_controller(self, controller):
        self.controller = controller

    def on_submit(self):
        self.controller.add_health_data()
        self.controller.load_history()
        self.controller.load_statistics()

    # ===== HIỂN THỊ =====
    def show_result(self, bmi, warnings):
    # 🔥 RESET MÀU (BƯỚC 4 NẰM Ở ĐÂY)
        self.result_label.config(fg="green")

        result = f"BMI: {bmi}\n"

        if warnings:
            result += "⚠ Cảnh báo:\n" + "\n".join(warnings)
        else:
            result += "✔ Sức khỏe bình thường"

        self.result_label.config(text=result)
    def show_history(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in data:
            self.tree.insert("", "end", values=(
                item["weight"],
                item["height"],
                item["bmi"],
                item["heart_rate"],
                item["co2"]
            ))

        self.draw_chart(data)

    def show_statistics(self, stats):
        if not stats:
            self.stats_label.config(text="Chưa có dữ liệu")
            return

        text = (
            f"Tổng số lần đo: {stats['total']}\n"
            f"BMI trung bình: {stats['avg_bmi']}\n"
            f"Nhịp tim TB: {stats['avg_heart']}\n"
            f"CO2 TB: {stats['avg_co2']}\n"
            f"Số lần bất thường: {stats['abnormal']}"
        )

        self.stats_label.config(text=text)

    def show_error(self, msg):
        messagebox.showerror("Lỗi", msg)

    def show_trend_warning(self, warnings):
        if not warnings:
            return

        msg = "CẢNH BÁO NGUY HIỂM:\n\n" + "\n".join(warnings)

        # popup
        messagebox.showwarning("Cảnh báo sức khỏe", msg)

        # đổi màu + in đậm
        self.result_label.config(fg="red", font=("Arial", 12, "bold"))
    # ===== BIỂU ĐỒ =====
    def draw_chart(self, data):
        self.ax.clear()

        if not data:
            self.canvas.draw()
            return

        bmi = [item["bmi"] for item in data]
        heart = [item["heart_rate"] for item in data]
        co2 = [item["co2"] for item in data]

        x = list(range(1, len(data) + 1))

        self.ax.plot(x, bmi, marker='o', color='#3498db', label="BMI")
        self.ax.plot(x, heart, marker='o', color='#e74c3c', label="Nhịp tim")
        self.ax.plot(x, co2, marker='o', color='#2ecc71', label="CO2")

        self.ax.set_title("Biểu đồ sức khỏe")
        self.ax.grid(True)
        self.ax.legend()

        self.canvas.draw()