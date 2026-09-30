class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


employee1 = Employee("Ravi", 30000)

print(employee1.get_name())
print(employee1.get_salary())

print()

employee1.set_name("Kiran")
employee1.set_salary(40000)

print(employee1.get_name())
print(employee1.get_salary())