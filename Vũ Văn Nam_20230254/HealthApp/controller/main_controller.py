from model.health_model import HealthModel


class MainController:
    def __init__(self, view):
        self.model = HealthModel()
        self.view = view

        # Load dữ liệu khi mở app
        self.load_history()
        self.load_statistics()

    # ================= THÊM DỮ LIỆU =================
    def add_health_data(self):
        try:
            weight = float(self.view.weight_var.get())
            height = float(self.view.height_var.get())
            heart = int(self.view.heart_var.get())
            co2 = int(self.view.co2_var.get())

            # Tính BMI
            bmi = self.model.calculate_bmi(weight, height)

            # Tạo record
            record = {
                "weight": weight,
                "height": height,
                "bmi": bmi,
                "heart_rate": heart,
                "co2": co2
            }

            # Lưu dữ liệu
            self.model.add_record(record)

            # Phân tích sức khỏe hiện tại
            warnings = self.model.analyze_health(record)

            # Lấy toàn bộ dữ liệu
            data = self.model.load_data()

            # Cảnh báo xu hướng (cũ)
            trend_warnings = self.model.detect_trend(data)

            # CẢNH BÁO BẤT THƯỜNG KHÔNG LIÊN TIẾP (BƯỚC 2)
            abnormal_warnings = self.model.detect_abnormal(data)

            all_warnings = trend_warnings + abnormal_warnings

            # Hiển thị
            self.view.show_result(bmi, warnings)
            self.view.show_trend_warning(all_warnings)

        except:
            self.view.show_error("Dữ liệu không hợp lệ!")

    # ================= LOAD BẢNG =================
    def load_history(self):
        data = self.model.load_data()
        self.view.show_history(data)

    # ================= LOAD THỐNG KÊ =================
    def load_statistics(self):
        stats = self.model.get_statistics()
        self.view.show_statistics(stats)