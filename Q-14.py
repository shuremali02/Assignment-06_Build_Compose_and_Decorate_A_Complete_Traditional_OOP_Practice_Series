# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, employee):
        self.employee = employee

    def show_employee(self):
        print(f"This department has employee: {self.employee.name}")
        
employee1=Employee("Ali")
dep=Department(employee1)
dep.show_employee()