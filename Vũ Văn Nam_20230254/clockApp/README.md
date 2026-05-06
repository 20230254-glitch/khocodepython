# ClockApp

Sinh viên thực hiện: **Vũ Văn Nam**

## Giới thiệu

ClockApp là ứng dụng đồng hồ và quản lý lịch được xây dựng bằng Python sử dụng thư viện Tkinter.
Ứng dụng cung cấp các chức năng xem thời gian, chuyển đổi múi giờ, hiển thị lịch, chuyển đổi âm lịch và nhắc lịch sự kiện theo thời gian thực.
---

##  Chức năng chính

###  1. Hiển thị thời gian hiện tại

* Đồng hồ chạy realtime (cập nhật mỗi giây)
* Có thể bật/tắt hiển thị giây

---

### 🌍2. Xem thời gian theo múi giờ

Người dùng có thể chọn các múi giờ:

* Asia/Ho_Chi_Minh
* UTC
* US/Eastern
* Europe/London
* Asia/Tokyo

---

### 3. Lịch và quản lý sự kiện

* Chọn ngày trực tiếp từ Calendar
* Thêm sự kiện theo ngày
* Xóa sự kiện đã tạo
* Hiển thị danh sách sự kiện

---

### 4. Chuyển đổi Âm lịch

* Cho phép chọn:

  * Dương lịch
  * Âm lịch
* Khi chọn âm lịch → hệ thống tự động chuyển đổi từ dương sang âm

---

### 5. Nhắc lịch theo thời gian thực

* Nhập sự kiện theo định dạng:

```
Nội dung | HH:MM
```

* Khi đến đúng thời gian → hệ thống hiển thị popup nhắc nhở

---

## Thư viện sử dụng

Cài đặt bằng pip:

```
pip install tkcalendar
pip install lunardate
pip install pytz
```

### Mô tả thư viện

| Thư viện   | Chức năng                            |
| ---------- | ------------------------------------ |
| tkinter    | Tạo giao diện người dùng             |
| tkcalendar | Hiển thị lịch                        |
| lunardate  | Chuyển đổi dương lịch sang âm lịch   |
| pytz       | Xử lý múi giờ                        |
| threading  | Chạy song song (đồng hồ & nhắc lịch) |

---

## Cách chạy chương trình

Mở terminal tại thư mục chứa file và chạy:

```
python main_view.py
```

---

##  Hướng dẫn test chương trình

### Test 1: Đồng hồ

* Chạy chương trình
* Quan sát thời gian cập nhật liên tục

---

### Test 2: Múi giờ

* Chọn múi giờ khác
* Thời gian sẽ thay đổi tương ứng

---

### Test 3: Âm lịch

* Chọn "Âm lịch"
* Thêm sự kiện khi nhập "test"
* Kiểm tra ngày hiển thị dạng âm lịch

---

### Test 4: Thêm sự kiện

Nhập:

```
Đi học | 07:30
```

→ Bấm **Thêm**

---

### Test 5: Nhắc lịch

* Nhập thời gian gần hiện tại (ví dụ sau 1–2 phút)
* Đợi đến giờ → popup thông báo sẽ xuất hiện

---

### Test 6: Xóa sự kiện

* Chọn sự kiện trong danh sách
* Bấm **Xóa**

---
### Đồng hồ

* Sử dụng `threading`
* Cập nhật mỗi giây bằng `datetime` + `pytz`

---

### Lịch

* Sử dụng `tkcalendar` để chọn ngày
* Trả về định dạng MM/DD/YY

---

### Âm lịch

* Sử dụng `lunardate`
* Chuyển đổi từ dương lịch sang âm lịch

---

### Nhắc lịch

* Lưu sự kiện dưới dạng `datetime`
* Thread chạy nền kiểm tra mỗi 30 giây
* Khi trùng thời gian → hiển thị thông báo

---

## Định dạng nhập dữ liệu

```
Nội dung | HH:MM
```

### Ví dụ:

```
Họp nhóm | 20:30
Đi học | 07:00
```

---

## Lưu ý

* Phải nhập đúng định dạng (có dấu `|`)
* Giờ phải theo định dạng 24h (HH:MM)
* Nhắc lịch có thể sai số ±30 giây do kiểm tra theo chu kỳ

---

## Kết luận

Ứng dụng đã đáp ứng đầy đủ yêu cầu:

* Xem thời gian
* Múi giờ
* Lịch
* Chuyển đổi âm lịch
* Nhắc lịch theo thời gian

Giao diện thân thiện, dễ sử dụng và có khả năng mở rộng thêm nhiều chức năng.

---
