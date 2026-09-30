class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)

employee1 = Employee("Ravi", 30000)

employee1.display()