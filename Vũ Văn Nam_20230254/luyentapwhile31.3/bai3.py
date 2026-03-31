n = int(input("Nhập n: "))

if n < 2:
    print("Không phải số nguyên tố")
else:
    i = 2
    check = True

    while i <= n // 2:
        if n % i == 0:
            check = False
            break
        i += 1

    if check:
        print("Đây là số nguyên tố")
    else:
        print("Không phải số nguyên tố")