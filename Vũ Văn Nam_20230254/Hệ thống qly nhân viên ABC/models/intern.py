from models.employee import Employee


class Intern(Employee):
    def calculate_salary(self):
        return self.base_salary + self.performance * 500