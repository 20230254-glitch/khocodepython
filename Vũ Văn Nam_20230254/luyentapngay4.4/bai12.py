_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

n = int(input("Nhập độ dài n: "))

dem = 0

for x in _list:
    if len(x) >= n and x[0] == x[-1]:
        dem += 1

print("Số chuỗi thỏa mãn:", dem)