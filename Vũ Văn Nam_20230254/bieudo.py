import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df = None

# ================= LOAD FILE =================
def load_file():
    global df

    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return

    try:
        df = pd.read_csv(file_path, encoding='latin1')

        # Xóa cột trùng
        df = df.loc[:, ~df.columns.duplicated()]
        df.columns = df.columns.str.strip()

        print("COLUMNS:", df.columns)

        # ===== DATE =====
        date_col = next((c for c in df.columns if "date" in c.lower()), None)
        if not date_col:
            raise Exception("Không tìm thấy cột ngày!")

        df[date_col] = pd.to_datetime(df[date_col])

        df["Month"] = df[date_col].dt.month
        df["Year"] = df[date_col].dt.year
        df["Quarter"] = df[date_col].dt.to_period("Q").astype(str)

        # ===== SALES =====
        sales_col = next((c for c in df.columns if "sale" in c.lower()), None)
        if not sales_col:
            raise Exception("Không tìm thấy cột doanh thu!")

        df.rename(columns={sales_col: "Sales"}, inplace=True)

        messagebox.showinfo("OK", "Load file thành công!")

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def draw_chart(data, kind, title, ylabel="Doanh thu (USD)"):

    for w in frame_chart.winfo_children():
        w.destroy()

    fig, ax = plt.subplots(figsize=(6,4))

    # ================= BAR =================
    if kind == "bar":
        data.plot(kind="bar", ax=ax)
        ax.set_ylabel(ylabel)

        ax.yaxis.set_major_formatter(
            mtick.StrMethodFormatter('{x:,.0f}')
        )

    # ================= LINE =================
    elif kind == "line":
        data.plot(kind="line", marker="o", ax=ax)
        ax.set_ylabel(ylabel)

        ax.yaxis.set_major_formatter(
            mtick.StrMethodFormatter('{x:,.0f}')
        )

    # ================= HORIZONTAL BAR (TOP SP) =================
    elif kind == "barh":
        data = data.sort_values()  # 👈 quan trọng để hiển thị đẹp
        data.plot(kind="barh", ax=ax)

        ax.set_xlabel(ylabel)

        ax.xaxis.set_major_formatter(
            mtick.StrMethodFormatter('{x:,.0f}')
        )

    # ================= PIE =================
    elif kind == "pie":
        data.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")

    ax.set_title(title)

    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame_chart)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


# ================= BIỂU ĐỒ =================
def plot_month():
    if df is None: return
    data = df.groupby("Month")["Sales"].sum()
    draw_chart(data, "line", "Doanh thu theo tháng", "Doanh thu (USD)")


def plot_year():
    if df is None: return
    data = df.groupby("Year")["Sales"].sum()
    draw_chart(data, "bar", "Doanh thu theo năm", "Doanh thu (USD)")


def plot_quarter():
    if df is None: return
    data = df.groupby("Quarter")["Sales"].sum()
    draw_chart(data, "bar", "Doanh thu theo quý", "Doanh thu (USD)")


def plot_product():
    if df is None:
        return

    col = "ProductName" if "ProductName" in df.columns else None

    if not col:
        col = next((c for c in df.columns if "product" in c.lower()), None)

    if not col:
        messagebox.showerror("Lỗi", "Không tìm thấy cột sản phẩm!")
        return

    data = (
        df.groupby(col)["Sales"]
        .sum()
        .sort_values(ascending=True) 
        .tail(10)
    )

    draw_chart(data, "barh", "Top 10 sản phẩm bán chạy", "Doanh thu (USD)")

def plot_region():
    if df is None: return

    col = next((c for c in df.columns if "region" in c.lower()), None)
    if not col:
        messagebox.showerror("Lỗi", "Không có cột Region!")
        return

    data = df.groupby(col)["Sales"].sum()
    draw_chart(data, "pie", "Doanh thu theo khu vực")

# ================= UI =================
root = tk.Tk()
root.title("🔥 DASHBOARD BÁN HÀNG PRO")
root.geometry("1000x650")

# ===== HEADER =====
header = tk.Frame(root, bg="#2c3e50", height=50)
header.pack(fill=tk.X)

tk.Label(header, text="📊 SALES DASHBOARD", fg="white",
         bg="#2c3e50", font=("Arial", 16, "bold")).pack(pady=10)

# ===== LEFT MENU =====
frame_left = tk.Frame(root, width=220, bg="#ecf0f1")
frame_left.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_left, text="MENU", bg="#ecf0f1",
         font=("Arial", 14, "bold")).pack(pady=10)

ttk.Button(frame_left, text="📂 Load CSV", command=load_file).pack(fill='x', pady=5)
ttk.Button(frame_left, text="📈 Doanh thu tháng", command=plot_month).pack(fill='x', pady=5)
ttk.Button(frame_left, text="📊 Doanh thu năm", command=plot_year).pack(fill='x', pady=5)
ttk.Button(frame_left, text="📆 Doanh thu quý", command=plot_quarter).pack(fill='x', pady=5)
ttk.Button(frame_left, text="🏆 Top sản phẩm", command=plot_product).pack(fill='x', pady=5)
ttk.Button(frame_left, text="🌍 Theo khu vực", command=plot_region).pack(fill='x', pady=5)

# ===== CHART AREA =====
frame_chart = tk.Frame(root, bg="white")
frame_chart.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()