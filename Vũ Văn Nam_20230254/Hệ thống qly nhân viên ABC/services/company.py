from exceptions.employee_exceptions import *
from models.developer import Developer
from models.manager import Manager
from models.intern import Intern


class Company:
    def __init__(self):
        self.employees = []

    # ================== THÊM NHÂN VIÊN ==================
    def add_employee(self, emp):
        emp_id = emp.emp_id.strip()

        for e in self.employees:
            if e.emp_id.strip() == emp_id:
                raise DuplicateEmployeeError("Trùng ID nhân viên")

        self.employees.append(emp)

    # ================== LẤY DANH SÁCH ==================
    def get_all(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        return self.employees

    # ================== TÌM KIẾM ==================
    def find_by_id(self, emp_id):
        emp_id = emp_id.strip()

        for e in self.employees:
            if e.emp_id.strip() == emp_id:
                return e

        raise EmployeeNotFoundError(emp_id)

    def find_by_name(self, name):
        name = name.strip().lower()
        return [e for e in self.employees if name in e.name.lower()]

    def find_developer_by_language(self, lang):
        lang = lang.strip().lower()

        return [
            e for e in self.employees
            if isinstance(e, Developer) and e.language.lower() == lang
        ]

    # ================== XÓA NHÂN VIÊN ==================
    def remove_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        self.employees.remove(emp)

    # ================== QUẢN LÝ DỰ ÁN ==================
    def assign_project(self, emp_id, project):
        emp = self.find_by_id(emp_id)
        project = project.strip()

        if not project:
            raise ProjectAllocationError("Tên dự án không được rỗng")

        # đảm bảo có thuộc tính
        if not hasattr(emp, "projects"):
            emp.projects = []

        if project in emp.projects:
            raise ProjectAllocationError("Dự án đã tồn tại")

        if len(emp.projects) >= 5:
            raise ProjectAllocationError("Mỗi nhân viên tối đa 5 dự án")

        emp.projects.append(project)

    def remove_project(self, emp_id, project):
        emp = self.find_by_id(emp_id)
        project = project.strip()

        if project not in emp.projects:
            raise ProjectAllocationError("Dự án không tồn tại")

        emp.projects.remove(project)

    # ================== HIỆU SUẤT ==================
    def update_performance(self, emp_id, score):
        if score < 0 or score > 10:
            raise ValueError("Điểm phải từ 0 đến 10")

        emp = self.find_by_id(emp_id)

        if not hasattr(emp, "performance"):
            emp.performance = 0

        emp.performance = score

    # ================== THĂNG CHỨC ==================
    def promote(self, emp_id):
        emp = self.find_by_id(emp_id)

        if isinstance(emp, Intern):
            new_emp = Developer(
                emp.emp_id,
                emp.name,
                emp.age,
                emp.email,
                emp.base_salary,
                "Python"
            )

        elif isinstance(emp, Developer):
            new_emp = Manager(
                emp.emp_id,
                emp.name,
                emp.age,
                emp.email,
                emp.base_salary
            )

        else:
            raise EmployeeException("Không thể thăng chức")

        # GIỮ LẠI DỮ LIỆU
        new_emp.projects = getattr(emp, "projects", [])
        new_emp.performance = getattr(emp, "performance", 0)

        self.remove_employee(emp_id)
        self.add_employee(new_emp)