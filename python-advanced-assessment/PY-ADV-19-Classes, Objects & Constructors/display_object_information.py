class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
student=Student("Seetha", 24)

print("Student Name:", student.name)
print("Student Age:", student.age)

print("=======================================================")

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

emp1=Employee("Neha", 80000)
emp2=Employee("Seetha", 90000)

print(emp1.name)
print(emp1.salary)
print()

print(emp2.name)
print(emp2.salary)