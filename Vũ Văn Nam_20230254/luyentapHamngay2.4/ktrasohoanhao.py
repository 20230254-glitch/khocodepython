def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

# Test
n = int(input("Nhập n: "))
if la_so_hoan_hao(n):
    print("Là số hoàn hảo")
else:
    print("Không phải số hoàn hảo")