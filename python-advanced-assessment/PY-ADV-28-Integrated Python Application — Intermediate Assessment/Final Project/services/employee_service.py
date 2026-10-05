from models.employee import Employee

from exceptions.custom_exceptions import (
    EmployeeAlreadyExistsError,
    EmployeeNotFoundError
)

from validators.employee_validators import (
    EmployeeValidator
)

class EmployeeService:

    def __init__(self, storage, logger):

        self.storage = storage
        self.logger = logger

        self.employees = self.storage.load_json()

    def add_employee(
        self,
        employee_id,
        name,
        age,
        email,
        salary,
        department,
        skills
    ):

        for employee in self.employees:

            if employee.employee_id == employee_id:

                raise EmployeeAlreadyExistsError(
                    "Employee ID already exists."
                )

        EmployeeValidator.validate(
            employee_id,
            name,
            age,
            email,
            salary,
            department,
            skills
        )

        employee = Employee(
            employee_id,
            name,
            int(age),
            email,
            float(salary),
            department,
            skills
        )

        self.employees.append(employee)

        self.storage.save_json(self.employees)

        self.logger.info(
            f"Employee added: {employee_id}"
        )

    def view_employees(self):

        return self.employees

    def search_employee(self, keyword):

        keyword = keyword.lower()

        results = []

        for employee in self.employees:

            if (
                keyword in employee.employee_id.lower()
                or keyword in employee.name.lower()
                or keyword in employee.email.lower()
            ):

                results.append(employee)

        return results

    def update_employee(
        self,
        employee_id,
        name,
        age,
        email,
        salary,
        department,
        skills
    ):

        employee = self.find_employee(employee_id)

        EmployeeValidator.validate(
            employee_id,
            name,
            age,
            email,
            salary,
            department,
            skills
        )

        employee.name = name
        employee.age = int(age)
        employee.email = email
        employee.salary = float(salary)
        employee.department = department
        employee.skills = skills

        self.storage.save_json(self.employees)

        self.logger.info(
            f"Employee updated: {employee_id}"
        )

    def delete_employee(self, employee_id):

        employee = self.find_employee(employee_id)

        self.employees.remove(employee)

        self.storage.save_json(self.employees)

        self.logger.info(
            f"Employee deleted: {employee_id}"
        )


    def find_employee(self, employee_id):

        for employee in self.employees:

            if employee.employee_id == employee_id:

                return employee

        raise EmployeeNotFoundError(
            "Employee not found."
        )
    
    def search_department(self, department):

        department = department.lower()

        return [
            employee
            for employee in self.employees
            if employee.department.lower() == department
        ]

    def search_skill(self, skill):

        skill = skill.lower()

        return [
            employee
            for employee in self.employees
            if any(
                skill == employee_skill.lower()
                for employee_skill in employee.skills
            )
        ]

    def generate_report(self):

        total = len(self.employees)

        if total == 0:
            return {
                "total_employees": 0,
                "average_salary": 0,
                "departments": {}
            }

        total_salary = sum(
            employee.salary
            for employee in self.employees
        )

        departments = {}

        for employee in self.employees:

            department = employee.department

            if department not in departments:
                departments[department] = 0

            departments[department] += 1

        return {
            "total_employees": total,
            "average_salary": total_salary / total,
            "departments": departments
        }
    def export_data(self):

        self.storage.export_csv(self.employees)

        self.logger.info(
            "Employee data exported to CSV."
        )