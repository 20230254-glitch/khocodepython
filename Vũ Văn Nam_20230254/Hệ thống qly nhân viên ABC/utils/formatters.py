def format_employee(emp):
    return f"""
ID: {emp.emp_id}
Tên: {emp.name}
Tuổi: {emp.age}
Email: {emp.email}
Loại: {emp.__class__.__name__}
Lương: {emp.calculate_salary()}
Hiệu suất: {emp.performance}
Dự án: {', '.join(emp.projects) if emp.projects else 'Không có'}
"""