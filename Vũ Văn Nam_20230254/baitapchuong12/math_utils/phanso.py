# phanso.py

def cong_ps(a, b, c, d):
    return (a*d + b*c, b*d)

def tru_ps(a, b, c, d):
    return (a*d - b*c, b*d)

def nhan_ps(a, b, c, d):
    return (a*c, b*d)

def chia_ps(a, b, c, d):
    if c == 0:
        raise ValueError("Không thể chia cho phân số có tử = 0")
    return (a*d, b*c)