from abc import ABC, abstractmethod
class InvalidEmployeeError(Exception):
    pass

class Employee(ABC):
    company_name = "BlackRoth"

    def __init__(self, emp_id, name, age, email, salary, department):
        self.__emp_id = emp_id
        self.__name = name
        self.__age = age
        self.__email = email
        self.__salary = salary
        self.__department = department

    # Encapsulation - Getters
    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @property
    def salary(self):
        return self.__salary

    @property
    def department(self):
        return self.__department

    # Setters
    def update_details(self, name, age, email, salary, department):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__salary = salary
        self.__department = department

    # Abstract method
    @abstractmethod
    def calculate_bonus(self):
        pass

    def calculate_salary(self):
        return self.__salary

    def display(self):
        print(
            self.__emp_id,
            self.__name,
            self.__age,
            self.__email,
            self.__salary,
            self.__department
        )

    # Class method
    @classmethod
    def company(cls):
        return cls.company_name

    # Static method
    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 60

class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.10

class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20

class HRManager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.15

class ValidationService:

    @staticmethod
    def validate_employee(emp_id, name, age, email, salary, department):

        if emp_id <= 0:
            raise InvalidEmployeeError("Employee ID must be positive")

        if not name:
            raise InvalidEmployeeError("Employee name cannot be empty")

        if not Employee.is_valid_age(age):
            raise InvalidEmployeeError("Age must be between 18 and 60")

        if "@" not in email:
            raise InvalidEmployeeError("Invalid email")

        if salary <= 0:
            raise InvalidEmployeeError("Salary must be positive")

        if not department:
            raise InvalidEmployeeError("Department cannot be empty")

class EmployeeService:

    def __init__(self):
        self.validation_service = ValidationService()
        self.employees = {}

# Add employee
    def add_employee(self, employee):

        ValidationService.validate_employee(
            employee.emp_id,
            employee.name,
            employee.age,
            employee.email,
            employee.salary,
            employee.department
        )

        if employee.emp_id in self.employees:
            raise InvalidEmployeeError("Employee ID already exists")

        self.employees[employee.emp_id] = employee

        print("Employee added successfully")

    # Update employee
    def update_employee(
        self,
        emp_id,
        name,
        age,
        email,
        salary,
        department
    ):

        if emp_id not in self.employees:
            raise InvalidEmployeeError("Employee not found")

        ValidationService.validate_employee(
            emp_id,
            name,
            age,
            email,
            salary,
            department
        )

        employee = self.employees[emp_id]

        employee.update_details(
            name,
            age,
            email,
            salary,
            department
        )

        print("Employee updated successfully")

    # Delete employee
    def delete_employee(self, emp_id):

        if emp_id not in self.employees:
            raise InvalidEmployeeError("Employee not found")

        del self.employees[emp_id]

        print("Employee deleted successfully")

    # Search employee
    def search_employee(self, emp_id):

        if emp_id in self.employees:
            return self.employees[emp_id]

        raise InvalidEmployeeError("Employee not found")

    # Display employees
    def display_employees(self):

        if not self.employees:
            print("No employees available")
            return

        for employee in self.employees.values():
            employee.display()

    # Search by department
    def search_by_department(self, department):

        found = False

        for employee in self.employees.values():

            if employee.department.lower() == department.lower():
                employee.display()
                found = True

        if not found:
            print("No employees found in this department")

# Calculate salary
    def calculate_salary(self, emp_id):
        employee = self.search_employee(emp_id)
        return employee.calculate_salary()

# Calculate bonus
    def calculate_bonus(self, emp_id):
        employee = self.search_employee(emp_id)
        return employee.calculate_bonus()

class ReportService:
    def generate_report(self, employee_service):
        print("\n========== EMPLOYEE REPORT ==========")

        for employee in employee_service.employees.values():
            salary = employee.calculate_salary()
            bonus = employee.calculate_bonus()

            print("Employee ID :", employee.emp_id)
            print("Name        :", employee.name)
            print("Department  :", employee.department)
            print("Salary      :", salary)
            print("Bonus       :", bonus)
            print("-------------------------------------")

def main():
    employee_service = EmployeeService()
    report_service = ReportService()

    try:
        employee1 = Developer(
            101,
            "Seetha",
            25,
            "seetha@gmail.com",
            70000,
            "Python"
        )

        employee2 = Manager(
            102,
            "Radha",
            30,
            "radha@gmail.com",
            80000,
            "Java"
        )

        employee3 = HRManager(
            103,
            "Priya",
            28,
            "priya@gmail.com",
            60000,
            "HR"
        )

# Add employees
        employee_service.add_employee(employee1)
        employee_service.add_employee(employee2)
        employee_service.add_employee(employee3)

# Display employees
        print("\nAll Employees:")
        employee_service.display_employees()

# Search employee
        print("\nSearch Employee:")

        employee = employee_service.search_employee(101)
        employee.display()

# Search by department
        print("\nSearch by Department:")

        employee_service.search_by_department("Python")

# Calculate salary

        print("\nSalary:")

        salary = employee_service.calculate_salary(101)

        print("Salary:", salary)

# Calculate bonus
        print("\nBonus:")

        bonus = employee_service.calculate_bonus(101)

        print("Bonus:", bonus)

# Update employee
        print("\nUpdating Employee:")

        employee_service.update_employee(
            101,
            "Seetha",
            26,
            "seetha@gmail.com",
            75000,
            "Python"
        )

# Delete employee

        print("\nDeleting Employee:")

        employee_service.delete_employee(103)

# Generate report
        report_service.generate_report(employee_service)

# Class method
        print("\nCompany:", Employee.company())

    except InvalidEmployeeError as e:

        print("Error:", e)

if __name__ == "__main__":
    main()