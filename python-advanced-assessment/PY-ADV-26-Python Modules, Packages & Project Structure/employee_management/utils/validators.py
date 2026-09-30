def validate_employee(employee_id, name, department, salary):

    if employee_id <= 0:
        raise ValueError("Employee ID must be greater than 0")

    if name == "":
        raise ValueError("Name cannot be empty")

    if department == "":
        raise ValueError("Department cannot be empty")

    if salary <= 0:
        raise ValueError("Salary must be greater than 0")

    return True