n = int(input("Nhập n (<20): "))

print("Các số chia hết cho 5 hoặc 7 là:")

for i in range(1, n + 1):
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")