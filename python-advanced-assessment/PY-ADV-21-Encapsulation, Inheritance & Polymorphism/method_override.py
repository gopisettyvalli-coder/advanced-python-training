class Parent:
    def show(self):
        print("This is parent method")

class Child(Parent):
    def show(self):
        print("This is child method")


obj = Child()
obj.show()

print("========================================")

# Another example
class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is testing code")

class Tester(Employee):
    def work(self):
        print("Tester is testing the code")

developer=Developer()
tester=Tester()

developer.work()
tester.work()