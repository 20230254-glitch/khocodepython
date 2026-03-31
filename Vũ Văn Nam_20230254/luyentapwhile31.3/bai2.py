n = int(input("Nhập n: "))

i = 1
tich = 1

while i <= n:
    tich = tich * i
    i += 1

print("n! =", tich)