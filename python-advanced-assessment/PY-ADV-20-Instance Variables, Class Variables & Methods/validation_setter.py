class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Name cannot be empty")

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be greater than 0")


employee1 = Employee("Ravi", 30000)

employee1.set_name("Kiran")
employee1.set_salary(40000)

print()

print(employee1.get_name())
print(employee1.get_salary())