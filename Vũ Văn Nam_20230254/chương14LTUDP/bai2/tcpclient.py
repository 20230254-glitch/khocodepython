import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8091

client_socket.connect((host, port))

# Nhập 2 số
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

# Gửi lên server dạng "a,b"
message = f"{a},{b}"
client_socket.send(message.encode('utf-8'))
print("CLIENT gửi:", message)

# Nhận kết quả
data = client_socket.recv(1024).decode('utf-8')
print("CLIENT nhận kết quả a + b =", data)

client_socket.close()