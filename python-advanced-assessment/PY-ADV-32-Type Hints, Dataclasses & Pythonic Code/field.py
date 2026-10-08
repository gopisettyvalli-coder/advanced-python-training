from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    skill: list= field(default_factory=list)

employee=Employee("Radha")
employee.skill.append("Python")

print(employee)