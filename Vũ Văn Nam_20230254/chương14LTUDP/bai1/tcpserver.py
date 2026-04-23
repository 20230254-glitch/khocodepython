import socket

# Tạo socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gắn IP và port
host = '127.0.0.1'  
port = 8090

server_socket.bind((host, port))

# Lắng nghe kết nối từ client
server_socket.listen(1)
print("SERVER đang chờ kết nối...")

# Chấp nhận kết nối
conn, addr = server_socket.accept()
print("Đã kết nối với:", addr)

# Nhận dữ liệu từ client
data = conn.recv(1024).decode('utf-8')
print("SERVER nhận:", data)

# Gửi phản hồi về client
message = "From SERVER TCP"
conn.send(message.encode('utf-8'))
print("SERVER gửi:", message)

conn.close()
server_socket.close()