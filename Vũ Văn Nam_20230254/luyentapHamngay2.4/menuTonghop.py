def tong_2_so(a, b):
    return a + b

def tong_nhieu_so(ds):
    return sum(ds)

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_snt(a, b):
    print("Các số nguyên tố:", end=" ")
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()

def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

def tim_so_hoan_hao(a, b):
    print("Các số hoàn hảo:", end=" ")
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")
    print()


# MENU
while True:
    print("\n===== MENU =====")
    print("1. Tổng 2 số")
    print("2. Tổng nhiều số")
    print("3. Kiểm tra SNT")
    print("4. Tìm SNT [a,b]")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm số hoàn hảo [a,b]")
    print("0. Thoát")

    chon = int(input("Chọn: "))

    if chon == 1:
        a = int(input("a = "))
        b = int(input("b = "))
        print("Kết quả:", tong_2_so(a, b))
        input("Nhấn Enter để tiếp tục...")

    elif chon == 2:
        n = int(input("Số lượng: "))
        ds = []
        for i in range(n):
            x = int(input(f"Nhập số {i+1}: "))
            ds.append(x)
        print("Kết quả:", tong_nhieu_so(ds))
        input("Nhấn Enter để tiếp tục...")

    elif chon == 3:
        n = int(input("n = "))
        if la_so_nguyen_to(n):
            print("→ Là số nguyên tố")
        else:
            print("→ Không phải số nguyên tố")
        input("Nhấn Enter để tiếp tục...")

    elif chon == 4:
        a = int(input("a = "))
        b = int(input("b = "))
        tim_snt(a, b)
        input("Nhấn Enter để tiếp tục...")

    elif chon == 5:
        n = int(input("n = "))
        if la_so_hoan_hao(n):
            print("→ Là số hoàn hảo")
        else:
            print("→ Không phải số hoàn hảo")
        input("Nhấn Enter để tiếp tục...")

    elif chon == 6:
        a = int(input("a = "))
        b = int(input("b = "))
        tim_so_hoan_hao(a, b)
        input("Nhấn Enter để tiếp tục...")

    elif chon == 0:
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!")