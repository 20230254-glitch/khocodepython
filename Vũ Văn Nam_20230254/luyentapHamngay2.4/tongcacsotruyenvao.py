def tong_nhieu_so(ds):
    tong = 0
    for x in ds:
        tong += x
    return tong

# Test
n = int(input("Nhập số lượng: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhập số thứ {i+1}: ")))

print("Tổng =", tong_nhieu_so(ds))