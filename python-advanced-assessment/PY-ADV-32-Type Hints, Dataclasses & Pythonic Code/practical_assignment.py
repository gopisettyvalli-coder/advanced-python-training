from dataclasses import dataclass

@dataclass
class Employee:
    employee_id: int
    name: str
    department: str
    salary: float
    experience: int

    def validate(self):
        if self.employee_id <=0:
            raise ValueError("Employee ID must be positive")

        if not self.name.strip():
            raise NameError("Name should not be empty")

        if self.salary<0:
            raise ValueError("Salary cannot be negative")

        if self.experience<0:
            raise ValueError("Experience cannot be negative")

        return True

# Calculate Annual Salary
    def calculate_annual_salary(self):
        return self.salary * 12

# Bonus Calaculation
    def calculate_bonus(self):
        if self.experience>=5:
            return self.salary * 0.20

        elif self.salary >=3:
            return self.salary * 0.10

        else:
            return self.salary*0.05

# Employee Reporting
    def generate_report(self):
        annual_salary=self.calculate_annual_salary()
        bonus= self.calculate_bonus()

        print("===== Employee Report =====")
        print(f"Employee_ID : {self.employee_id}")
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")
        print(f"Monthly Salary : ${self.salary:2f}")
        print(f"Experience : {self.experience}years")
        print(f"Annual Salary : ${self.salary:2f}")
        print(f"Bonus : ${bonus:2f}")
        print(f"Total Earnings : ${annual_salary+bonus:2f}")

# Creating Employee Object
employee=Employee(
    employee_id = 101,
    name="Siva",
    department="Python",
    salary=6,
    experience=5
)

try:
    employee.validate()
    print("Employee validation successful")

    employee.generate_report()

except ValueError as error:
    print("Validation Error", error)