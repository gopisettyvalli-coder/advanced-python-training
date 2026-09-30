class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

employee1=Employee("Seetha", 70000)
employee2=Employee("Radha", 80000)

print(employee1.name)
print(employee1.salary)

print()

print(employee2.name)
print(employee2.salary)

print("===============================================")


class Cars:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

car1=Cars("BMW", "Blsck")
car2=Cars("Thar", "Black")

print(car1.brand)
print(car1.color)

print()

print(car2.brand)
print(car2.color)