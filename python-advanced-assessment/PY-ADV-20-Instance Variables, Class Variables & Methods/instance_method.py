class Employee:
    company="Blackroth" 

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

emp1=Employee("Seetha", 70000)
emp2=Employee("Radha", 80000)

emp1.display_details()
print(emp1.company)
print()
emp2.display_details()

