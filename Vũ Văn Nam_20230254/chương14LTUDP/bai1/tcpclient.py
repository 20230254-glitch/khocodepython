import socket

# Tạo socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8090

# Kết nối tới server
client_socket.connect((host, port))

# Gửi dữ liệu lên server
message = "From CLIENT TCP"
client_socket.send(message.encode('utf-8'))
print("CLIENT gửi:", message)

# Nhận phản hồi từ server
data = client_socket.recv(1024).decode('utf-8')
print("CLIENT nhận:", data)

client_socket.close()