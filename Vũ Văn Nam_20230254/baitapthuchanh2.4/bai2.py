
text = input("Nhập đoạn văn: ")

with open("test.txt", "w", encoding="utf-8") as f:
    f.write(text)

# đọc lại và in ra
with open("test.txt", "r", encoding="utf-8") as f:
    print("Nội dung file:")
    print(f.read())