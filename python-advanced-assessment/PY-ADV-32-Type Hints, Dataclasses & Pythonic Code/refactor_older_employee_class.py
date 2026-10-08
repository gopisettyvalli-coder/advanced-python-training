# Before Dataclass
class Employee:
    def __init__(self, name, salary, age):
        self.name=name
        self.salary=salary
        self.age=age

    def display(self):
        return f"{self.name}, {self.salary}, {self.age}"

employee=Employee("Seetha", 80000, 29)

print(employee.name)
print(employee.salary)
print(employee.age)
print()


# After dataclass
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float
    age: int

employee= Employee("Radha", 90000, 30)

print(employee)
print()
print(employee.name)
print(employee.salary)
print(employee.age)