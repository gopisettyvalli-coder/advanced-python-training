from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: float
    marks: int

student=Student("Radha", 23, 80)
print(student)
