class Employee:
    company_name="Blackroth"
    company_location="Hyderabad"
    employee_count=0

    def __init__(self,employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        Employee.employee_count += 1

# Get employee count
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

# Get company details
    @classmethod
    def get_company_details(cls):
        return cls.company_name, cls.company_location

# Validate salary
    def validate_salary(self):
        if self.salary > 0:
            return True
        else:
            return False

# Calculate bonus
    def calculate_bonus(self):
        if self.salary >= 50000:
            return self.salary * 0.10
        else:
            return self.salary * 0.05

# Static method to validate email
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

# Static method to validate salary
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

# Alternative constructor
    @classmethod
    def from_string(cls, data):
        employee_id, name, department, salary = data.split(",")

        return cls(
            int(employee_id),
            name,
            department,
            float(salary)
        )

# Creating Employee objects
employee1 = Employee(101, "John", "Python", 50000)
employee2 = Employee(102, "Ravi", "Testing", 40000)

# Employee details
print("Employee 1:")
print("ID:", employee1.employee_id)
print("Name:", employee1.name)
print("Department:", employee1.department)
print("Salary:", employee1.salary)

print("\nSalary Valid:", employee1.validate_salary())
print("Bonus:", employee1.calculate_bonus())

# Employee count
print("\nTotal Employees:", Employee.get_employee_count())

# Company details
print("Company Name:", Employee.get_company_details()[0])
print("Company Location:", Employee.get_company_details()[1])

# Static methods
print("\nEmail Valid:", Employee.is_valid_email("john@gmail.com"))
print("Salary Valid:", Employee.is_valid_salary(50000))

# Alternative constructor
employee3 = Employee.from_string("103,David,Python,60000")

print("\nEmployee 3:")
print("ID:", employee3.employee_id)
print("Name:", employee3.name)
print("Department:", employee3.department)
print("Salary:", employee3.salary)

print("\nTotal Employees:", Employee.get_employee_count())