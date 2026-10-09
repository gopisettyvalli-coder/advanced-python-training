import csv

from storage.file_manager import EmployeeFileManager
from utils.decorators import log_execution, measure_time

class EmployeeService:
    def __init__(self, filename="data/employees.csv"):
        self.filename = filename

    @log_execution
    @measure_time
    def save_employees(self, employees):
        fieldnames = [
            "employee_id",
            "name",
            "department",
            "salary",
            "experience",
        ]

        with EmployeeFileManager(self.filename, "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for employee in employees:
                writer.writerow({
                    "employee_id": employee.employee_id,
                    "name": employee.name,
                    "department": employee.department,
                    "salary": employee.salary,
                    "experience": employee.experience,
                })

        print("Employees saved successfully.")

    @log_execution
    def load_employees(self):
        employees = []

        with EmployeeFileManager(self.filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                employees.append({
                    "employee_id": int(row["employee_id"]),
                    "name": row["name"],
                    "department": row["department"],
                    "salary": float(row["salary"]),
                    "experience": int(row["experience"]),
                })

        return employees