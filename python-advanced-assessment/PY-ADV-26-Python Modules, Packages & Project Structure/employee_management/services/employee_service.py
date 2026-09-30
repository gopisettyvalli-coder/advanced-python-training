from models.employee import Employee
from utils.validators import validate_employee
from utils.helpers import find_employee
from exceptions.employee_exceptions import EmployeeNotFoundException

class EmployeeService:

    def __init__(self, storage_file):
        self.storage_file = storage_file

    def add_employee(self, employee_id, name, department, salary):

        validate_employee(employee_id, name, department, salary)

        employees = self.load_employees()

        if find_employee(employees, employee_id):
            raise ValueError("Employee already exists")

        employee = Employee(
            employee_id,
            name,
            department,
            salary
        )

        employees.append(employee.to_dict())

        self.save_employees(employees)

        print("Employee added successfully")

    def view_employees(self):

        employees = self.load_employees()

        if not employees:
            print("No employees found")
            return

        for employee in employees:
            print(employee)

    def search_employee(self, employee_id):

        employees = self.load_employees()

        employee = find_employee(employees, employee_id)

        if employee is None:
            raise EmployeeNotFoundException("Employee not found")

        print(employee)

    def update_employee(self, employee_id, name, department, salary):

        employees = self.load_employees()

        employee = find_employee(employees, employee_id)

        if employee is None:
            raise EmployeeNotFoundException("Employee not found")

        validate_employee(employee_id, name, department, salary)

        employee["name"] = name
        employee["department"] = department
        employee["salary"] = salary

        self.save_employees(employees)

        print("Employee updated successfully")

    def delete_employee(self, employee_id):

        employees = self.load_employees()

        employee = find_employee(employees, employee_id)

        if employee is None:
            raise EmployeeNotFoundException("Employee not found")

        employees.remove(employee)

        self.save_employees(employees)

        print("Employee deleted successfully")

    def load_employees(self):

        from storage.json_storage import load_employees

        return load_employees(self.storage_file)

    def save_employees(self, employees):

        from storage.json_storage import save_employees

        save_employees(self.storage_file, employees)