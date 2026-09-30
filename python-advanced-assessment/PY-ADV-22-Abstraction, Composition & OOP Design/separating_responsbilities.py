# Without separating responsabilities
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        pass

    def save_to_database(self):
        pass

    def send_email(self):
        pass

# With Separating Responsibilities
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(self.name, self.salary)

class EmployeeRepository:
    def save(self, employee):
        print("Employee saved to database")

class EmailService:
    def send_mail(self, employee):
        print("Email sent to:", employee.name)

