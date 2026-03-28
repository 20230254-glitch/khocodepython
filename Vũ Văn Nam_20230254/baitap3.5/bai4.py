_so = int(input("Nhap vao so nguyen duong n: "))
if _so % 2 == 0:
    if _so % 3 == 0:
        print(_so, "chia het cho 2 va 3")
    else:
        print(_so, "chia het cho 2 nhung khong chia het cho 3")
elif _so % 3 == 0:
    print(_so, "chia het cho 3 nhung khong chia het cho 2")