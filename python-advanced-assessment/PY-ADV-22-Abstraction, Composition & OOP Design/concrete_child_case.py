from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee salary:", self.salary)
 
    @abstractmethod
    def calculate_bonus(self):
        pass

class Developer(Employee):
    def calculate_bonus(self):
        bonus=self.salary*0.10
        print("Bonus:", bonus)

class Manager(Employee):
    def calculate_bonus(self):
        bonus=self.salary*0.20
        print("Bonus:", bonus)

developer=Developer("Seetha", 70000)
manager=Manager("Siva", 80000)

developer.display()
developer.calculate_bonus()

print()

manager.display()
manager.calculate_bonus()