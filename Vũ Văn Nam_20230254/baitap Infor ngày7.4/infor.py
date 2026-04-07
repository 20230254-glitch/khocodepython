class HocVien:
    def __init__(self, ht, ngaysinh, email, dt, dc, lop):
        self.hoten = ht
        self.ngaysinh = ngaysinh
        self.email = email
        self.dienthoai = dt
        self.diachi = dc
        self.lop = lop

# b) trả về thông tin
    def show_info(self):
        return f"""Họ tên: {self.hoten}
Ngày sinh: {self.ngaysinh}
Email: {self.email}
Điện thoại: {self.dienthoai}
Địa chỉ: {self.diachi}
Lớp: {self.lop}"""

# c) đổi thông tin
    def change_info(self, dc="Hà Nội", lop="IT12.x"):
        self.diachi = dc
        self.lop = lop

# d) chương trình chính
hv1 = HocVien("Vũ Văn Nam", "2005-02-07", "nam@gmail.com", "09087262", "Ninh Bình", "IT14.1")
# tạo đối tượng hv1 với thông tin đã cho
print(hv1.show_info())
print("------------")
#gọi phương thức thay đổi thông tin với giá trị mặc định
hv1.change_info()
print(hv1.show_info())
print("------------")
#gọi phương thức thay đổi thông tin với giá trị mới
hv1.change_info("Hà Tĩnh", "IT14.2")
print(hv1.show_info())