import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8091

server_socket.bind((host, port))
server_socket.listen(1)

print("SERVER đang chờ kết nối...")

conn, addr = server_socket.accept()
print("Đã kết nối với:", addr)

# Nhận dữ liệu từ client (dạng "a,b")
data = conn.recv(1024).decode('utf-8')
print("SERVER nhận:", data)

# Tách 2 số
a, b = map(int, data.split(","))

# Tính tổng
tong = a + b
print("SERVER tính tổng:", tong)

# Gửi kết quả về client
conn.send(str(tong).encode('utf-8'))

conn.close()
server_socket.close()