class Employee:
    def __init__(self, name, salary):
        self._name = name         # protected-style
        self.__salary = salary    # private-style

    def display(self):
        print("Name:", self._name)
        print("Salary:", self.__salary)

employee1 = Employee("Ravi", 30000)

employee1.display()