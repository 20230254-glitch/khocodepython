class EmployeeException(Exception):
    pass

class EmployeeNotFoundError(EmployeeException):
    def __init__(self, employee_id):
        super().__init__(f"Không tìm thấy nhân viên có ID: {employee_id}")

class InvalidSalaryError(EmployeeException):
    pass

class InvalidAgeError(EmployeeException):
    pass

class ProjectAllocationError(EmployeeException):
    pass

class DuplicateEmployeeError(EmployeeException):
    pass