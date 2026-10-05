import re

from exceptions.custom_exceptions import InvalidEmployeeError

class EmployeeValidator:

    @staticmethod
    def validate(
        employee_id,
        name,
        age,
        email,
        salary,
        department,
        skills
    ):

        if not employee_id:
            raise InvalidEmployeeError(
                "Employee ID cannot be empty."
            )

        if not name:
            raise InvalidEmployeeError(
                "Name cannot be empty."
            )

        try:
            age = int(age)
        except ValueError:
            raise InvalidEmployeeError(
                "Age must be a number."
            )

        if age < 18 or age > 60:
            raise InvalidEmployeeError(
                "Age must be between 18 and 60."
            )

        try:
            salary = float(salary)
        except ValueError:
            raise InvalidEmployeeError(
                "Salary must be a number."
            )

        if salary <= 0:
            raise InvalidEmployeeError(
                "Salary must be greater than 0."
            )

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern, email):
            raise InvalidEmployeeError(
                "Invalid email address."
            )

        if not department:
            raise InvalidEmployeeError(
                "Department cannot be empty."
            )

        if not skills:
            raise InvalidEmployeeError(
                "At least one skill is required."
            )

        return True