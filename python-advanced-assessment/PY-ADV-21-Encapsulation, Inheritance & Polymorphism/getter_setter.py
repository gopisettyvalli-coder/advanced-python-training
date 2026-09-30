class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

employee1 = Employee("Ravi", 30000)
print(employee1.get_salary())
employee1.set_salary(40000)
print(employee1.get_salary())