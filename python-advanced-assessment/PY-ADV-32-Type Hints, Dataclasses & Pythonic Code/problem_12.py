# NORMAL CLASS
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

employee=Employee("Neha", 80000)

print(employee.name)
print(employee.salary)

print()

# DATA CLASS
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float

employee=Employee("Reethu", 80000)

print(employee.name)
print(employee.salary)