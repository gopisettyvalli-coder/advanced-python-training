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

    def update_details(self, name, age, email, salary, department):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__salary = salary
        self.__department = department

    @abstractmethod
    def calculate_bonus(self):
        pass

    def calculate_salary(self):
        return self.__salary

    def display(self):
        print(
            self.emp_id, self.name, self.age,
            self.email, self.salary, self.department
        )

    @classmethod
    def company(cls):
        return cls.company_name

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
    def validate_employee(
        self, emp_id, name, age, email, salary, department
    ):
        if emp_id <= 0:
            raise InvalidEmployeeError("Employee ID must be positive")

        if not name or not name.strip():
            raise InvalidEmployeeError("Employee name cannot be empty")

        if not Employee.is_valid_age(age):
            raise InvalidEmployeeError("Age must be between 18 and 60")

        if not email or "@" not in email:
            raise InvalidEmployeeError("Invalid email")

        if salary <= 0:
            raise InvalidEmployeeError("Salary must be positive")

        if not department or not department.strip():
            raise InvalidEmployeeError("Department cannot be empty")

class EmployeeService:
    def __init__(self, validation_service=None):
        self.validation_service = (
            validation_service or ValidationService()
        )
        self.__employees = {}

    def add_employee(self, employee):
        self.validation_service.validate_employee(
            employee.emp_id, employee.name, employee.age,
            employee.email, employee.salary, employee.department
        )

        if employee.emp_id in self.__employees:
            raise InvalidEmployeeError("Employee ID already exists")

        self.__employees[employee.emp_id] = employee
        print("Employee added successfully")

    def update_employee(
        self, emp_id, name, age, email, salary, department
    ):
        employee = self.search_employee(emp_id)

        self.validation_service.validate_employee(
            emp_id, name, age, email, salary, department
        )

        employee.update_details(name, age, email, salary, department)
        print("Employee updated successfully")

    def delete_employee(self, emp_id):
        if emp_id not in self.__employees:
            raise InvalidEmployeeError("Employee not found")

        del self.__employees[emp_id]
        print("Employee deleted successfully")

    def search_employee(self, emp_id):
        if emp_id not in self.__employees:
            raise InvalidEmployeeError("Employee not found")
       
        return self.__employees[emp_id]

    def get_all_employees(self):
        return tuple(self.__employees.values())

    def display_employees(self):
        employees = self.get_all_employees()

        if not employees:
            print("No employees available")
            return

        for employee in employees:
            employee.display()

    def search_by_department(self, department):
        found = False

        for employee in self.get_all_employees():
            if employee.department.lower() == department.lower():
                employee.display()
                found = True

        if not found:
            print("No employees found in this department")

    def calculate_salary(self, emp_id):
        return self.search_employee(emp_id).calculate_salary()

    def calculate_bonus(self, emp_id):
        return self.search_employee(emp_id).calculate_bonus()

class ReportService:
    def generate_report(self, employees):
        print("\n========== EMPLOYEE REPORT ==========")

        for employee in employees:
            print("Employee ID :", employee.emp_id)
            print("Name        :", employee.name)
            print("Department  :", employee.department)
            print("Salary      :", employee.calculate_salary())
            print("Bonus       :", employee.calculate_bonus())
            print("-------------------------------------")

def main():
    validator = ValidationService()
    employee_service = EmployeeService(validator)
    report_service = ReportService()

    try:
        employee1 = Developer(
            101, "Seetha", 25, "seetha@gmail.com", 70000, "Python"
        )
        employee2 = Manager(
            102, "Radha", 30, "radha@gmail.com", 80000, "Java"
        )
        employee3 = HRManager(
            103, "Priya", 28, "priya@gmail.com", 60000, "HR"
        )

        employee_service.add_employee(employee1)
        employee_service.add_employee(employee2)
        employee_service.add_employee(employee3)

        print("\nAll Employees:")
        employee_service.display_employees()

        print("\nSearch Employee:")
        employee_service.search_employee(101).display()

        print("\nSearch by Department:")
        employee_service.search_by_department("Python")

        print("\nSalary:", employee_service.calculate_salary(101))
        print("Bonus:", employee_service.calculate_bonus(101))

        print("\nUpdating Employee:")
        employee_service.update_employee(
            101, "Seetha", 26, "seetha@gmail.com", 75000, "Python"
        )

        print("\nDeleting Employee:")
        employee_service.delete_employee(103)

        report_service.generate_report(
            employee_service.get_all_employees()
        )

        print("\nCompany:", Employee.company())

    except InvalidEmployeeError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()