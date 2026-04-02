# Bước 1: Ghi file
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO\n")

# Bước 2: In ra 1 dòng
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("In 1 dòng:")
    print(content.replace("\n", " "))

# Bước 3: In từng dòng
with open("demo.txt", "r", encoding="utf-8") as f:
    print("In từng dòng:")
    for line in f:
        print(line.strip())