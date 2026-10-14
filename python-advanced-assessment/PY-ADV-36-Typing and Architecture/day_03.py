from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import wraps
from time import perf_counter
from typing import Optional, Tuple, List, Dict, Iterator
from typing_extensions import Protocol
import logging

# Logging Configuration
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# Custom Exception
class InvalidEmployeeError(Exception):
    pass

# Decorators
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Executing: %s", func.__name__)
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        logger.info("Execution time: %.6f seconds", elapsed)
        return result
    return wrapper

# Employee Dataclass
@dataclass
class Employee(ABC):
    emp_id: int
    name: str
    age: int
    email: str
    salary: float
    department: str
    company_name = "Blackroth"

    def update_details(
        self,name: str, age: int, email: str, salary: float, department: str
    ) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.salary = salary
        self.department = department

    def calculate_salary(self) -> float:
        return self.salary

    @abstractmethod
    def calculate_bonus(self) -> float:
        pass

    @staticmethod
    def is_valid_age(age: int) -> bool:
        return 18 <= age <= 60

    @classmethod
    def company(cls) -> str:
        return cls.company_name

# Employee Types
@dataclass
class Developer(Employee):
    def calculate_bonus(self) -> float:
        return self.salary * 0.40

@dataclass
class Manager(Employee):
    def calculate_bonus(self) -> float:
        return self.salary * 0.20

@dataclass
class HRManager(Employee):
    def calculate_bonus(self) -> float:
        return self.salary * 0.15

# Storage Protocol
class EmployeeStorage(Protocol):
    def add(self, employee: Employee) -> None:
        ...

    def find(self, emp_id: int) -> Employee:
        ...

    def update(self, employee: Employee) -> None:
        ...

    def delete(self, emp_id: int) -> None:
        ...

    def get_all(self) -> Tuple[Employee, ...]:
        ...

# In-Memory Storage
class InMemoryEmployeeStorage:
    def __init__(self) -> None:
        self._employees: Dict[int, Employee] = {}

    def add(self, employee: Employee) -> None:
        if employee.emp_id in self._employees:
            raise InvalidEmployeeError("Employee ID already exists")
        self._employees[employee.emp_id] = employee

    def find(self, emp_id: int) -> Employee:
        if emp_id not in self._employees:
            raise InvalidEmployeeError("Employee not found")
        return self._employees[emp_id]

    def update(self, employee: Employee) -> None:
        if employee.emp_id not in self._employees:
            raise InvalidEmployeeError("Employee not found")
        self._employees[employee.emp_id] = employee

    def delete(self, emp_id: int) -> None:
        if emp_id not in self._employees:
            raise InvalidEmployeeError("Employee not found")
        del self._employees[emp_id]

    def get_all(self) -> Tuple[Employee, ...]:
        return tuple(self._employees.values())

# Validation Service
class ValidationService:
    def validate_employee(
        self,
        emp_id: int,
        name: str,
        age: int,
        email: str,
        salary: float,
        department: str
    ) -> None:
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

# Employee Service
class EmployeeService:
    def __init__(
        self,
        validation_service: Optional[ValidationService] = None,
        storage: Optional[EmployeeStorage] = None
    ) -> None:
        self.validation_service = (
            validation_service or ValidationService()
        )
        self.storage: EmployeeStorage = (
            storage or InMemoryEmployeeStorage()
        )

    def _validate(self, employee: Employee) -> None:
        self.validation_service.validate_employee(
            employee.emp_id,
            employee.name,
            employee.age,
            employee.email,
            employee.salary,
            employee.department
        )

    @log_execution
    def add_employee(self, employee: Employee) -> None:
        self._validate(employee)
        self.storage.add(employee)

    @log_execution
    def update_employee(
        self,
        emp_id: int,
        name: str,
        age: int,
        email: str,
        salary: float,
        department: str
    ) -> Employee:
        old_employee = self.storage.find(emp_id)

        updated_employee = type(old_employee)(
            emp_id, name, age, email, salary, department
        )

        self._validate(updated_employee)
        self.storage.update(updated_employee)
        return updated_employee

    def delete_employee(self, emp_id: int) -> None:
        self.storage.delete(emp_id)

    def search_employee(self, emp_id: int) -> Employee:
        return self.storage.find(emp_id)

    def get_all_employees(self) -> Tuple[Employee, ...]:
        return self.storage.get_all()

    def generate_employees(self) -> Iterator[Employee]:
        for employee in self.storage.get_all():
            yield employee

    def search_by_department(
        self, department: str
    ) -> List[Employee]:
        return [
            employee
            for employee in self.generate_employees()
            if employee.department.casefold() == department.casefold()
        ]

    def get_high_salary_employees(self) -> List[Employee]:
        return [
            employee
            for employee in self.generate_employees()
            if employee.salary > 50000
        ]

    def calculate_salary(self, emp_id: int) -> float:
        return self.search_employee(emp_id).calculate_salary()

    def calculate_bonus(self, emp_id: int) -> float:
        return self.search_employee(emp_id).calculate_bonus()

# Report Service
class ReportService:
    def generate_report(
        self, employees: Iterator[Employee]
    ) -> str:
        lines = ["========== EMPLOYEE REPORT =========="]

        for employee in employees:
            lines.extend([
                "Employee ID : {}".format(employee.emp_id),
                "Name        : {}".format(employee.name),
                "Department  : {}".format(employee.department),
                "Salary      : {:.2f}".format(employee.salary),
                "Bonus       : {:.2f}".format(
                    employee.calculate_bonus()
                ),
                "-------------------------------------"
            ])

        return "\n".join(lines)

    @measure_time
    def display_report(
        self, employees: Iterator[Employee]
    ) -> None:
        print(self.generate_report(employees))

    @log_execution
    def export_employees(
        self,
        employees: Iterator[Employee],
        filename: str = "employee_report.txt"
    ) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            for employee in employees:
                file.write(
                    "ID: {}, Name: {}, Department: {}, "
                    "Salary: {:.2f}, Bonus: {:.2f}\n".format(
                        employee.emp_id,
                        employee.name,
                        employee.department,
                        employee.salary,
                        employee.calculate_bonus()
                    )
                )

# Display Employee
def display_employee(employee: Employee) -> None:
    print(
        "ID: {} | Name: {} | Age: {} | Email: {} | "
        "Salary: {:.2f} | Department: {}".format(
            employee.emp_id,
            employee.name,
            employee.age,
            employee.email,
            employee.salary,
            employee.department
        )
    )

def main() -> None:
    employee_service = EmployeeService()
    report_service = ReportService()

    try:
        employees = (
            Developer(
                101, "Seetha", 25,
                "seetha@gmail.com", 70000, "Python"
            ),
            Manager(
                102, "Radha", 30,
                "radha@gmail.com", 80000, "Java"
            ),
            HRManager(
                103, "Priya", 28,
                "priya@gmail.com", 60000, "HR"
            )
        )

# Add Employees
        for employee in employees:
            employee_service.add_employee(employee)

        print("\nEmployees added successfully.")

# Display All Employees
        print("\nAll Employees:")
        for employee in employee_service.get_all_employees():
            display_employee(employee)

# Search Employee
        print("\nSearch Employee:")
        display_employee(employee_service.search_employee(101))

# Search by Department
        print("\nPython Department Employees:")
        for employee in employee_service.search_by_department("Python"):
            display_employee(employee)

# High Salary Employees
        print("\nEmployees with Salary Above 50000:")
        for employee in employee_service.get_high_salary_employees():
            display_employee(employee)

# Salary and Bonus
        print("\nSalary:", employee_service.calculate_salary(101))
        print("Bonus:", employee_service.calculate_bonus(101))

# Update Employee
        print("\nUpdating Employee:")
        updated = employee_service.update_employee(
            101, "Seetha", 26,
            "seetha@gmail.com", 75000, "Python"
        )
        display_employee(updated)

# Generate Report
        print("\nGenerating Report:")
        report_service.display_report(
            iter(employee_service.get_all_employees())
        )

# Export Report
        report_service.export_employees(
            iter(employee_service.get_all_employees())
        )
        print("\nEmployee report exported successfully.")

# Delete Employee
        employee_service.delete_employee(103)
        print("\nEmployee deleted successfully.")

# Display Remaining Employees
        print("\nEmployees After Deletion:")
        for employee in employee_service.get_all_employees():
            display_employee(employee)

        print("\nCompany:", Employee.company())

    except InvalidEmployeeError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
