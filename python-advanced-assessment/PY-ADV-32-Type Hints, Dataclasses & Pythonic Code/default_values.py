from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str= "Python"

employee= Employee("Seetha")
print(employee)