#nhập và lưu file
info = {}
info["ten"] = input("Tên: ")
info["tuoi"] = input("Tuổi: ")
info["email"] = input("Email: ")
info["skype"] = input("Skype: ")
info["diachi"] = input("Địa chỉ: ")
info["noilam"] = input("Nơi làm việc: ")

with open("setInfo.txt", "w", encoding="utf-8") as f:
    for key, value in info.items():
        f.write(f"{key}: {value}\n")
#đọc và hiển thị file
with open("setInfo.txt", "r", encoding="utf-8") as f:
    print("Thông tin cá nhân:")
    print(f.read())
