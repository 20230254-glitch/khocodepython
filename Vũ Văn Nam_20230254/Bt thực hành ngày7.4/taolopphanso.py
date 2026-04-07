import math
import tkinter as tk
from tkinter import messagebox

# ================== CLASS PHÂN SỐ ==================
class PhanSo:
    def __init__(self, tu, mau=1):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0!")
        self.tu = tu
        self.mau = mau

    def toi_gian(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        if self.mau < 0:  # chuẩn hóa dấu
            self.tu *= -1
            self.mau *= -1
        return self

    def cong(self, ps):
        return PhanSo(self.tu * ps.mau + ps.tu * self.mau,
                      self.mau * ps.mau).toi_gian()

    def tru(self, ps):
        return PhanSo(self.tu * ps.mau - ps.tu * self.mau,
                      self.mau * ps.mau).toi_gian()

    def nhan(self, ps):
        return PhanSo(self.tu * ps.tu,
                      self.mau * ps.mau).toi_gian()

    def chia(self, ps):
        if ps.tu == 0:
            raise ValueError("Không thể chia cho phân số có tử = 0!")
        return PhanSo(self.tu * ps.mau,
                      self.mau * ps.tu).toi_gian()

    def so_sanh(self, ps):
        if self.tu * ps.mau > ps.tu * self.mau:
            return ">"
        elif self.tu * ps.mau < ps.tu * self.mau:
            return "<"
        else:
            return "="

    def gia_tri(self):
        return self.tu / self.mau

    def hien_thi(self):
        return f"{self.tu}/{self.mau}"


# ================== NHẬP TỪ BÀN PHÍM ==================
def nhap_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    return PhanSo(tu, mau)


# ================== DEMO CONSOLE ==================
def demo_console():
    print("=== NHẬP 2 PHÂN SỐ ===")
    ps1 = nhap_phan_so()
    ps2 = nhap_phan_so()

    print("Cộng:", ps1.cong(ps2).hien_thi())
    print("Trừ:", ps1.tru(ps2).hien_thi())
    print("Nhân:", ps1.nhan(ps2).hien_thi())
    print("Chia:", ps1.chia(ps2).hien_thi())

    print("So sánh:", ps1.hien_thi(), ps1.so_sanh(ps2), ps2.hien_thi())

    # Sắp xếp
    ds = [ps1, ps2, PhanSo(3, 4), PhanSo(5, 6)]
    ds.sort(key=lambda x: x.gia_tri())

    print("Danh sách sau sắp xếp:")
    for ps in ds:
        print(ps.hien_thi())


# ================== GUI TKINTER ==================
def mo_gui():
    def tinh_toan(phep):
        try:
            ps1 = PhanSo(int(entry_tu1.get()), int(entry_mau1.get()))
            ps2 = PhanSo(int(entry_tu2.get()), int(entry_mau2.get()))

            if phep == "+":
                kq = ps1.cong(ps2)
            elif phep == "-":
                kq = ps1.tru(ps2)
            elif phep == "*":
                kq = ps1.nhan(ps2)
            elif phep == "/":
                kq = ps1.chia(ps2)

            label_kq.config(text="Kết quả: " + kq.hien_thi())

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def so_sanh_gui():
        try:
            ps1 = PhanSo(int(entry_tu1.get()), int(entry_mau1.get()))
            ps2 = PhanSo(int(entry_tu2.get()), int(entry_mau2.get()))

            kq = ps1.so_sanh(ps2)
            label_kq.config(text=f"So sánh: {ps1.hien_thi()} {kq} {ps2.hien_thi()}")

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    root = tk.Tk()
    root.title("Máy tính phân số")

    # Nhập PS1
    tk.Label(root, text="Phân số 1").grid(row=0, column=0)
    entry_tu1 = tk.Entry(root, width=5)
    entry_mau1 = tk.Entry(root, width=5)
    entry_tu1.grid(row=0, column=1)
    entry_mau1.grid(row=0, column=2)

    # Nhập PS2
    tk.Label(root, text="Phân số 2").grid(row=1, column=0)
    entry_tu2 = tk.Entry(root, width=5)
    entry_mau2 = tk.Entry(root, width=5)
    entry_tu2.grid(row=1, column=1)
    entry_mau2.grid(row=1, column=2)

    # Nút phép toán
    tk.Button(root, text="+", command=lambda: tinh_toan("+")).grid(row=2, column=0)
    tk.Button(root, text="-", command=lambda: tinh_toan("-")).grid(row=2, column=1)
    tk.Button(root, text="*", command=lambda: tinh_toan("*")).grid(row=2, column=2)
    tk.Button(root, text="/", command=lambda: tinh_toan("/")).grid(row=2, column=3)

    # Nút so sánh
    tk.Button(root, text="So sánh", command=so_sanh_gui).grid(row=3, column=0, columnspan=4)

    label_kq = tk.Label(root, text="Kết quả:", fg="blue")
    label_kq.grid(row=4, column=0, columnspan=4)

    root.mainloop()


# ================== CHẠY CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    print("1. Chạy console")
    print("2. Mở giao diện GUI")
    chon = input("Chọn (1/2): ")

    if chon == "1":
        demo_console()
    else:
        mo_gui()