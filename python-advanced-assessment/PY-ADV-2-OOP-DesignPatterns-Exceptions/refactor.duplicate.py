class Employee:

    def calculate_amount(self, salary, percentage):
        return salary * percentage

    def calculate_bonus(self, salary):
        bonus = self.calculate_amount(salary, 0.10)
        print("Bonus:", bonus)

    def calculate_tax(self, salary):
        tax = self.calculate_amount(salary, 0.10)
        print("Tax:", tax)

employee = Employee()
employee.calculate_bonus(30000)
employee.calculate_tax(30000)