class Student:
    school= "ABC School"

    def __init__(self, name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

student1=Student("Seetha", 22, 95)
student2=Student("Radha", 24, 80)

print(student1.name)
print(student1.school)

print()

print(student2.name)
print(student2.school)

# Employee class variable
class Employee:
    company="Blackroth"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

emp1=Employee("Seetha", 70000)
emp2=Employee("Raadha", 85000)

print(emp1.name)
print(emp1.company)

print()

print(emp2.name)
print(emp2.company)