class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(self.name, self.salary)

emp1=Employee("Seetha", 70000)
emp2=Employee("Radha", 80000)

emp1.display()
emp2.display()