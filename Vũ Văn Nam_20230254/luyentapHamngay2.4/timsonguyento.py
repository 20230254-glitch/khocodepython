def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_snt(a, b):
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")

# Test
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Các số nguyên tố:")
tim_snt(a, b)