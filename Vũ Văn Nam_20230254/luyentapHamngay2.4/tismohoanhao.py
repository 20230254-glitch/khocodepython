def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

def tim_so_hoan_hao(a, b):
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")

# Test
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Các số hoàn hảo:")
tim_so_hoan_hao(a, b)