# main.py

from math_utils import *

# ===== PHÂN SỐ =====
a, b = 1, 2
c, d = 3, 4

print("Cộng:", cong_ps(a, b, c, d))
print("Trừ:", tru_ps(a, b, c, d))
print("Nhân:", nhan_ps(a, b, c, d))
print("Chia:", chia_ps(a, b, c, d))


# ===== HÌNH HỌC =====
dai = 5
rong = 3
r = 2

print("Chu vi HCN:", chu_vi_hinh_chu_nhat(dai, rong))
print("Diện tích HCN:", dien_tich_hinh_chu_nhat(dai, rong))

print("Chu vi hình tròn:", chu_vi_hinh_tron(r))
print("Diện tích hình tròn:", dien_tich_hinh_tron(r))