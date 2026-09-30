from abc import ABC, abstractmethod

class Employee(ABC):
    def display(self):
        print("This is an employee")

    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary calculated")

class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary calculated")

developer = Developer()
manager = Manager()

developer.display()
developer.calculate_salary()

manager.display()
manager.calculate_salary()