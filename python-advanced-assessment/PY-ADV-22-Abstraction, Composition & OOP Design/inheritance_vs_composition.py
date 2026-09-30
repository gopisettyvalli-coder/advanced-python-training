# Inheritance
class Employee:
    def display(self):
        print("Employee")

class Developer(Employee):
    pass

developer = Developer()
developer.display()

print("====================================")

#Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

car = Car()
car.engine.start()
