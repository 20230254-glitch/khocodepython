import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

def fmt(x):
    return int(x) if x.is_integer() else round(x, 2)

# Trường hợp a = 0 (phương trình bậc 1)
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Nghiệm x =", fmt(x))
else:
    delta = b*b - 4*a*c
    
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", fmt(x))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm:")
        print("x1 =", fmt(x1))
        print("x2 =", fmt(x2))