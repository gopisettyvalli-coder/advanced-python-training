class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
emp=Employee("Valli", 90000)

print(emp.name)
print(emp.salary)

emp.name="Seetha"
emp.salary=80000

print("Employee Name:",emp.name)
print("Employee Salary:", emp.salary)