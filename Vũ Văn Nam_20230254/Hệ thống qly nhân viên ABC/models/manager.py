from models.employee import Employee

class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary * 2 + self.performance * 100