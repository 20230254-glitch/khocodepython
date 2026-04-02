#tạo file
with open("demo_file2.txt", "w", encoding="utf-8") as f:
    f.write("Dem so luong tu xuat hien abc abc abc 12 12 it it dnu eaut")
#Đếm từ
with open("demo_file2.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
count = {}

for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

print(count)