import csv
import os

from generators.employee_generator import generate_employees
from services.employee_service import EmployeeService
from reports.report_generator import generate_report

def main():
    try:
        os.makedirs("data", exist_ok=True)

        employees = list(generate_employees())

        service = EmployeeService()
        service.save_employees(employees)

        loaded_employees = service.load_employees()

        generate_report(loaded_employees)

    except (ValueError, OSError, csv.Error) as error:
        print(f"Application error: {error}")

if __name__ == "__main__":
    main()