class Employee:

    def work(self):
        print("Employee is working")

class Developer(Employee):

    def write_code(self):
        print("Developer is writing code")

developer = Developer()
developer.work()
developer.write_code()