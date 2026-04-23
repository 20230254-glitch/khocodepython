import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8092))

# Nhập danh sách mật khẩu
data = input("Nhập các mật khẩu (cách nhau bằng dấu phẩy): ")

client_socket.send(data.encode('utf-8'))
print("CLIENT gửi:", data)

# Nhận kết quả
result = client_socket.recv(1024).decode('utf-8')

print("Mật khẩu hợp lệ:", result)

client_socket.close()