class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class SalaryCalculator:
    def calculate_bonus(self, employee):
        return employee.salary * 0.10

class EmployeeRepository:
    def save(self, employee):
        print("Employee saved to database")

class EmailService:
    def send_email(self, employee):
        print("Email sent to", employee.name)

employee=Employee("Seetha", 80000)

calculator = SalaryCalculator()
print(calculator.calculate_bonus(employee))

repository = EmployeeRepository()
repository.save(employee)

email = EmailService()
email.send_email(employee)