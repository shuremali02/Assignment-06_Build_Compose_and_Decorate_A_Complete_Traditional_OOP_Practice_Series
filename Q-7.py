# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee():
    def __init__(self,name,salary,ssn):
        self.name=name
        self._salary=salary
        self.__ssn=ssn
access=Employee("Ali",25000,"123-45-678")
print(f"Employee Name:{access.name}")
print(f"Employee Salary: {access._salary}") 
print(f"Employee Ssn: {access.__ssn} ") # this line give a AttributeError due to name mangling
# print(f"Employee ssn: {access._Employee__ssn}") uncomment this line to see the employee ssn  