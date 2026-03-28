import time

nam_sinh = int(input("Nhập năm sinh: "))

x = time.localtime()
nam_hien_tai = x[0]

tuoi = nam_hien_tai - nam_sinh

print("Năm sinh", nam_sinh, ", vậy thì bạn", tuoi, "tuổi")