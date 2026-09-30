from abc import ABC, abstractmethod

class Employee(ABC):
    def display(self):
        print("This is an employee")

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary is 50000")

class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary is 80000")

developer = Developer()
manager = Manager()

developer.display()
developer.calculate_salary()

manager.display()
manager.calculate_salary()