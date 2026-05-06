HEALTH MONITORING SYSTEM - HƯỚNG DẪN SỬ DỤNG

========================================

1. GIỚI THIỆU
   ========================================
   Đây là ứng dụng theo dõi sức khỏe được xây dựng bằng Python theo mô hình MVC.

Chức năng chính:

* Nhập dữ liệu sức khỏe (cân nặng, chiều cao, nhịp tim, CO2)
* Tính BMI tự động
* Lưu lịch sử vào file JSON
* Hiển thị bảng dữ liệu
* Thống kê trung bình
* Vẽ biểu đồ trực quan
* Cảnh báo sức khỏe thông minh

========================================
2. CẤU TRÚC DỰ ÁN
=================

HealthApp/
│
├── main.py
├── model/
│   └── health_model.py
├── view/
│   └── main_view.py
├── controller/
│   └── main_controller.py
├── data/
│   └── health_data.json
└── README.txt

========================================
3. THƯ VIỆN SỬ DỤNG
===================

1. tkinter

* Tạo giao diện GUI
* Các thành phần:

  * Tk() → tạo cửa sổ
  * Frame → chia layout
  * Label → hiển thị text
  * Entry → nhập dữ liệu
  * Button → nút bấm
  * Treeview → bảng dữ liệu

2. matplotlib

* Vẽ biểu đồ
* Các hàm:

  * plt.subplots() → tạo biểu đồ
  * ax.plot() → vẽ đường
  * ax.set_title() → tiêu đề
  * ax.grid() → lưới
  * canvas.draw() → cập nhật

3. json

* Lưu dữ liệu
* json.load() → đọc file
* json.dump() → ghi file

4. os

* Quản lý file/thư mục
* os.path.exists()
* os.makedirs()

========================================
4. CÁCH CHẠY ỨNG DỤNG
=====================

Bước 1: Cài Python (>= 3.10)

Bước 2: Cài thư viện
Mở terminal và chạy:
pip install matplotlib

Bước 3: Chạy chương trình
cd tới thư mục project:
cd d:\LTUDP\HealthApp

Chạy:
python main.py

========================================
5. CÁCH SỬ DỤNG
===============

* Nhập:

  * Cân nặng (kg)
  * Chiều cao (cm)
  * Nhịp tim
  * CO2

* Bấm "Phân tích"

Kết quả:

* BMI hiển thị
* Cảnh báo nếu bất thường
* Dữ liệu lưu vào bảng
* Biểu đồ cập nhật

========================================
6. TÍNH NĂNG THÔNG MINH 
=================================

1. Phân tích sức khỏe:

* BMI (thiếu cân / thừa cân)
* Nhịp tim thấp / cao
* CO2 nguy hiểm

2. Cảnh báo xu hướng:

* BMI tăng liên tục
* Nhịp tim tăng dần
* CO2 tăng dần

3. Phát hiện bất thường:

* Nhịp tim tăng đột biến
* BMI thay đổi mạnh
* CO2 tăng bất thường

4. Biểu đồ trực quan:

* Theo dõi thay đổi theo thời gian
* 3 đường: BMI / Heart / CO2

5. Lưu dữ liệu:

* Không mất dữ liệu khi tắt app

========================================

7. LỖI THƯỜNG GẶP
=================

1. Không chạy được:
   → chưa cài matplotlib

2. Lỗi file JSON:
   → kiểm tra thư mục data

3. Không hiển thị dữ liệu:
   → kiểm tra controller

4. Lỗi indent:
   → Python rất nhạy khoảng trắng
========================================
END
===
