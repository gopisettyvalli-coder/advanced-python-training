from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float
    age: int

employee=Employee("Seetha", 800000, 28)
print(employee)
