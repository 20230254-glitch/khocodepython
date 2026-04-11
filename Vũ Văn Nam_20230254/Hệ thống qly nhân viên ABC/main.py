from models import Manager, Developer, Intern
from services import Company
from services.payroll import *
from utils.validators import *

company = Company()

# ================== 1. THÊM NHÂN VIÊN ==================
def add_employee():
    try:
        emp_id = input("ID: ")
        name = input("Tên: ")
        age = int(input("Tuổi: "))
        validate_age(age)

        email = input("Email: ")
        validate_email(email)

        salary = float(input("Lương cơ bản: "))
        validate_salary(salary)

        print("a. Manager\nb. Developer\nc. Intern")
        choice = input("Chọn: ")

        if choice == "a":
            emp = Manager(emp_id, name, age, email, salary)
        elif choice == "b":
            lang = input("Ngôn ngữ: ")
            emp = Developer(emp_id, name, age, email, salary, lang)
        else:
            emp = Intern(emp_id, name, age, email, salary)

        company.add_employee(emp)
        print("✔ Thêm thành công:", emp)

    except Exception as e:
        print("❌ Lỗi:", e)


# ================== 2. HIỂN THỊ ==================
def show_menu():
    print("a. Tất cả\nb. Theo loại\nc. Theo hiệu suất")
    choice = input("Chọn: ")

    try:
        if choice == "a":
            for e in company.get_all():
                print(e, "| Lương:", e.calculate_salary())

        elif choice == "b":
            t = input("Nhập loại (Manager/Developer/Intern): ")
            for e in company.employees:
                if e.__class__.__name__ == t:
                    print(e)

        elif choice == "c":
            sorted_list = sorted(company.employees, key=lambda x: x.performance, reverse=True)
            for e in sorted_list:
                print(e, "| Điểm:", e.performance)

    except Exception as e:
        print(e)


# ================== 3. TÌM KIẾM ==================
def find_menu():
    print("a. Theo ID\nb. Theo tên\nc. Theo ngôn ngữ")
    choice = input("Chọn: ")

    try:
        if choice == "a":
            emp_id = input("ID: ")
            print(company.find_by_id(emp_id))

        elif choice == "b":
            name = input("Tên: ")
            for e in company.find_by_name(name):
                print(e)

        elif choice == "c":
            lang = input("Ngôn ngữ: ")
            for e in company.find_developer_by_language(lang):
                print(e)

    except Exception as e:
        print(e)


# ================== 4. LƯƠNG ==================
def salary_menu():
    print("a. Lương từng NV\nb. Tổng lương\nc. Top 3")
    choice = input("Chọn: ")

    if choice == "a":
        for e in company.employees:
            print(e, "| Lương:", e.calculate_salary())

    elif choice == "b":
        print("Tổng:", total_salary(company.employees))

    elif choice == "c":
        for e in top_3_salary(company.employees):
            print(e, "|", e.calculate_salary())


# ================== 5. DỰ ÁN ==================
def project_menu():
    print("a. Thêm dự án\nb. Xóa dự án\nc. Xem dự án")
    choice = input("Chọn: ")

    try:
        emp_id = input("ID: ")

        if choice == "a":
            project = input("Tên dự án: ")
            company.assign_project(emp_id, project)

        elif choice == "b":
            project = input("Tên dự án: ")
            company.remove_project(emp_id, project)

        elif choice == "c":
            emp = company.find_by_id(emp_id)
            print("Dự án:", emp.projects)

    except Exception as e:
        print(e)


# ================== 6. HIỆU SUẤT ==================
def performance_menu():
    print("a. Cập nhật\nb. Xuất sắc\nc. Cần cải thiện")
    choice = input("Chọn: ")

    try:
        if choice == "a":
            emp_id = input("ID: ")
            score = float(input("Điểm: "))
            company.update_performance(emp_id, score)

        elif choice == "b":
            for e in company.employees:
                if e.performance > 8:
                    print(e)

        elif choice == "c":
            for e in company.employees:
                if e.performance < 5:
                    print(e)

    except Exception as e:
        print(e)


# ================== 7. NHÂN SỰ ==================
def hr_menu():
    print("a. Xóa NV\nb. Tăng lương\nc. Thăng chức")
    choice = input("Chọn: ")

    try:
        emp_id = input("ID: ")

        if choice == "a":
            company.remove_employee(emp_id)

        elif choice == "b":
            emp = company.find_by_id(emp_id)
            inc = float(input("Tăng thêm: "))
            emp.base_salary += inc
            print("✔ Đã tăng lương")

        elif choice == "c":
            company.promote(emp_id)

    except Exception as e:
        print(e)


# ================== 8. THỐNG KÊ ==================
def report_menu():
    print("a. Số lượng theo loại\nb. Tổng lương\nc. TB dự án")
    choice = input("Chọn: ")

    if choice == "a":
        print(count_by_type(company.employees))

    elif choice == "b":
        print("Tổng lương:", total_salary(company.employees))

    elif choice == "c":
        print("TB dự án:", avg_projects(company.employees))


# ================== MENU CHÍNH ==================
def menu():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ NHÂN VIÊN =====")
        print("1. Thêm nhân viên")
        print("2. Hiển thị")
        print("3. Tìm kiếm")
        print("4. Lương")
        print("5. Dự án")
        print("6. Hiệu suất")
        print("7. Nhân sự")
        print("8. Thống kê")
        print("9. Thoát")

        choice = input("Chọn (1-9): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            show_menu()
        elif choice == "3":
            find_menu()
        elif choice == "4":
            salary_menu()
        elif choice == "5":
            project_menu()
        elif choice == "6":
            performance_menu()
        elif choice == "7":
            hr_menu()
        elif choice == "8":
            report_menu()
        elif choice == "9":
            print("Thoát chương trình")
            break
        else:
            print("Sai lựa chọn!")


if __name__ == "__main__":
    menu()