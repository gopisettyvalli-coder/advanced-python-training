class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def get_employee_name(self):
        return self.__name

    def update_employee_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Name cannot be empty")

    def get_employee_salary(self):
        return self.__salary

    def update_employee_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be greater than 0")


employee1 = Employee("Ravi", 30000)

print(employee1.get_employee_name())
print(employee1.get_employee_salary())

employee1.update_employee_name("Kiran")
employee1.update_employee_salary(40000)

print(employee1.get_employee_name())
print(employee1.get_employee_salary())