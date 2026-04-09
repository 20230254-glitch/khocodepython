from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, age, email, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.projects = []
        self.performance = 0

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.__class__.__name__}"