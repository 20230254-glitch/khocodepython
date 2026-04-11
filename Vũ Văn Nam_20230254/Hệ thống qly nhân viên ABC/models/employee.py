from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, name, age, email, base_salary):
        # ===== CHUẨN HÓA DỮ LIỆU =====
        self.emp_id = emp_id.strip()
        self.name = name.strip()
        self.age = age
        self.email = email.strip()
        self.base_salary = base_salary

        # ===== THUỘC TÍNH HỆ THỐNG =====
        self.projects = []        # danh sách dự án
        self.performance = 0      # điểm hiệu suất (0-10)

    # ===== PHƯƠNG THỨC TRỪU TƯỢNG =====
    @abstractmethod
    def calculate_salary(self):
        pass

    # ===== HIỂN THỊ THÔNG TIN =====
    def __str__(self):
        return (
            f"ID: {self.emp_id} | "
            f"Tên: {self.name} | "
            f"Loại: {self.__class__.__name__} | "
            f"Lương cơ bản: {self.base_salary} | "
            f"Hiệu suất: {self.performance} | "
            f"Số dự án: {len(self.projects)}"
        )

    def display(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "type": self.__class__.__name__,
            "salary": self.calculate_salary(),
            "projects": len(self.projects),
            "performance": self.performance
        }