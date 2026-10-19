from exceptions import InvalidEmployeeError

def validate_employee(
    emp_id: int,
    name: str,
    age: int,
    email: str,
) -> None:

    if not isinstance(emp_id, int) or isinstance(emp_id, bool) or emp_id <= 0:
        raise InvalidEmployeeError("Employee ID must be a positive integer")

    if not isinstance(name, str) or not name.strip():
        raise InvalidEmployeeError("Name cannot be empty")

    if not isinstance(age, int) or isinstance(age, bool) or age < 18:
        raise InvalidEmployeeError("Employee must be at least 18")

    if not isinstance(email, str):
        raise InvalidEmployeeError("Invalid email address")

    email = email.strip()
    parts = email.split("@")

    if (
        len(parts) != 2
        or not parts[0]
        or not parts[1]
        or any(char.isspace() for char in email)
        or "." not in parts[1]
        or parts[1].startswith(".")
        or parts[1].endswith(".")
    ):
        raise InvalidEmployeeError("Invalid email address")