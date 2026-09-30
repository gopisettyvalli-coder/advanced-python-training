class Employee:
    def TeamLead(self):
        print("Sai is the team lead")

    def Manager(Employee):
        print("Edukondalu is the manager")

emp=Employee()
emp.TeamLead()
emp.Manager()

print("============================================")

# Single-level Inheritance
class Vehicle:
    def Car(self):
        print("The brand of the car is BMW")

    def Bike(Vehicle):
        print("The color of the bike is black")

car=Vehicle()

car.Car()
car.Bike()

print("===================================================")

# Multiple Inheritance
class Father:
    def work(self):
        print("Father is working")

class Mother:
    def cook(self):
        print("Mother is cooking")

class Child(Father,Mother):
    def study(self):
        print("Child is studying")

child=Child()

child.cook()
child.work()
child.study()
print("=========================================================")

# Multi-level Inheritance

class Animal:
    def bark(self):
        print("Dog is barking")

class Dog(Animal):
    def eat(self):
        print("Dog eats chicken")

class Puppy(Dog):
    def play(self):
        print("Playing")

puppy=Puppy()

puppy.bark()
puppy.eat()
puppy.play()
