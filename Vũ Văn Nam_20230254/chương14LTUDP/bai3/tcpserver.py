import socket
import re

def is_valid_password(pw):
    if len(pw) < 6 or len(pw) > 12:
        return False
    if not re.search("[a-z]", pw):
        return False
    if not re.search("[A-Z]", pw):
        return False
    if not re.search("[0-9]", pw):
        return False
    if not re.search("[$#@]", pw):
        return False
    return True


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8092))
server_socket.listen(1)

print("SERVER đang chờ kết nối...")

conn, addr = server_socket.accept()
print("Đã kết nối:", addr)

# Nhận chuỗi mật khẩu
data = conn.recv(1024).decode('utf-8')
print("SERVER nhận:", data)

# Tách danh sách mật khẩu
passwords = data.split(",")

# Lọc mật khẩu hợp lệ
valid_passwords = [pw for pw in passwords if is_valid_password(pw)]

# Ghép lại chuỗi trả về
result = ",".join(valid_passwords)

print("SERVER trả về:", result)

conn.send(result.encode('utf-8'))

conn.close()
server_socket.close()