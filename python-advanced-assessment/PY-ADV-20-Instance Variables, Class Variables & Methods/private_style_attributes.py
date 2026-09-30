class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

employee1 = Employee("Ravi", 30000)

print(employee1.__name)