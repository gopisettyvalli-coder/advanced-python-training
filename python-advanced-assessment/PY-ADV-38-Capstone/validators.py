from exceptions import InvalidEmployeeError

def validate_employee(emp_id, name, age, email):
    if not isinstance(emp_id, int) or isinstance(emp_id, bool) or emp_id <= 0:
        raise InvalidEmployeeError("Employee ID must be positive")

    if not isinstance(name, str) or not name.strip():
        raise InvalidEmployeeError("Name cannot be empty")

    if not isinstance(age, int) or isinstance(age, bool) or age < 18:
        raise InvalidEmployeeError("Employee must be at least 18")

    if (
        not isinstance(email, str)
        or "@" not in email
        or not email.split("@", 1)[1]
    ):
        raise InvalidEmployeeError("Invalid email address")