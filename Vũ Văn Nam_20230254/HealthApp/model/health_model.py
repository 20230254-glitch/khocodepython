import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "health_data.json")


class HealthModel:
    def __init__(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

    def load_data(self):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def save_data(self, data):
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_record(self, record):
        data = self.load_data()
        data.append(record)
        self.save_data(data)

    def calculate_bmi(self, weight, height):
        try:
            height_m = height / 100
            return round(weight / (height_m ** 2), 2)
        except:
            return 0

    # ================= PHÂN TÍCH CHUẨN Y KHOA =================
    def analyze_health(self, record):
        warnings = []

        bmi = record["bmi"]
        heart = record["heart_rate"]
        co2 = record["co2"]

        # BMI chuẩn WHO
        if bmi < 18.5:
            warnings.append("Thiếu cân")
        elif 18.5 <= bmi < 25:
            warnings.append("BMI bình thường")
        elif 25 <= bmi < 30:
            warnings.append("Thừa cân")
        else:
            warnings.append("Béo phì (nguy cơ cao)")

        # Nhịp tim (người trưởng thành)
        if heart < 60:
            warnings.append("Nhịp tim thấp (Bradycardia)")
        elif 60 <= heart <= 100:
            pass  # bình thường
        else:
            warnings.append("Nhịp tim cao (Tachycardia)")

        # CO2 (ppm - môi trường)
        if co2 < 400:
            warnings.append("CO2 thấp bất thường")
        elif 400 <= co2 <= 1000:
            pass  # bình thường
        elif 1000 < co2 <= 2000:
            warnings.append("CO2 cao - không khí kém")
        else:
            warnings.append("CO2 rất cao - nguy hiểm")

        return warnings
    
    def detect_trend(self, data):
        if len(data) < 3:
            return []

        warnings = []

        last3 = data[-3:]

        bmi_list = [d["bmi"] for d in last3]
        heart_list = [d["heart_rate"] for d in last3]
        co2_list = [d["co2"] for d in last3]

        # BMI tăng liên tục
        if bmi_list[0] < bmi_list[1] < bmi_list[2]:
            warnings.append("BMI tăng liên tục (nguy cơ béo phì)")

        # Nhịp tim tăng
        if heart_list[0] < heart_list[1] < heart_list[2]:
            warnings.append("Nhịp tim tăng dần (nguy cơ tim mạch)")

        # CO2 tăng
        if co2_list[0] < co2_list[1] < co2_list[2]:
            warnings.append("CO2 tăng dần (môi trường xấu)")

        return warnings
    
    def detect_abnormal(self, data):
        if len(data) < 2:
            return []

        warnings = []

        latest = data[-1]
        prev = data[-2]

        # BMI tăng đột biến
        if abs(latest["bmi"] - prev["bmi"]) > 3:
            warnings.append("BMI thay đổi bất thường")

        # Nhịp tim đột biến
        if abs(latest["heart_rate"] - prev["heart_rate"]) > 20:
            warnings.append("Nhịp tim biến động mạnh")

        # CO2 tăng đột biến
        if abs(latest["co2"] - prev["co2"]) > 300:
            warnings.append("CO2 tăng đột ngột")

        return warnings

    # ================= THỐNG KÊ =================
    def get_statistics(self):
        data = self.load_data()

        if not data:
            return None

        total_bmi = sum(item["bmi"] for item in data)
        total_heart = sum(item["heart_rate"] for item in data)
        total_co2 = sum(item["co2"] for item in data)

        abnormal_count = 0
        for item in data:
            result = self.analyze_health(item)

            # nếu có cảnh báo nguy hiểm thì tính bất thường
            if any("nguy hiểm" in r.lower() or "cao" in r.lower() or "thấp" in r.lower() for r in result):
                abnormal_count += 1

        return {
            "avg_bmi": round(total_bmi / len(data), 2),
            "avg_heart": round(total_heart / len(data), 2),
            "avg_co2": round(total_co2 / len(data), 2),
            "total": len(data),
            "abnormal": abnormal_count
        }