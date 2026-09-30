class Employee:
    def __init__(self,id, name, salary, department):
        self.id=id
        self.name=name
        self.salary=salary
        self.department=department

    def display_details(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee Department:", self.department)

    def calaculate_bonus(self):
        return self.salary*0.05

class Developer(Employee):
    def __init__(self,id,name,salary,department,programming_language,projects):
        super().__init__(id,name,salary,department)
        self.programming_language=programming_language
        self.projects=projects

    def calaculate_bonus(self):
        return self.salary*0.10

class Manager(Employee):
    def __init__(self,id,name,salary,department,team_size,management_bonus):
        super().__init__(id,name,salary,department)
        self.team_size=team_size
        self.management_bonus=management_bonus

    def calaculate_bonus(self):
        return self.salary*0.15 + self.management_bonus

class HRManager(Employee):
    def __init__(self,id,name,salary,department,employees_handled):
        super().__init__(id,name,salary,department)
        self.employees_handled=employees_handled

    def calaculate_bonus(self):
        return self.salary*0.08

employees=[
    Developer(101, "Seetha", 50000, "IT", "Python", 3),
    Manager(102, "Ravi", 60000, "Management", 10, 5000),
    HRManager(103, "Shreya", 80000, "HR", 20)
]

for employee in employees:
    employee.display_details()
    print("Bonus:", employee.calaculate_bonus())
    print()


    