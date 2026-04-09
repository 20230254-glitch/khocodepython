from exceptions.employee_exceptions import *

def validate_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError()

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError()

def validate_email(email):
    if "@" not in email:
        raise ValueError("Email không hợp lệ")