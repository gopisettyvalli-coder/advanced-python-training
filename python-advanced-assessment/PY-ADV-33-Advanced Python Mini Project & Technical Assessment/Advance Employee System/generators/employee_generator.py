from models.employee import Employee

def generate_employees():
    employee_data = [
        (101, "Seetha", "Python", 70000, 3),
        (102, "Radha", "Java", 80000, 6),
        (103, "Siva", "Testing", 50000, 2),
        (104, "Ram", "Python", 90000, 8),
        (105, "Reethu", "HR", 60000, 4),
    ]

    for data in employee_data:
        yield Employee(*data)