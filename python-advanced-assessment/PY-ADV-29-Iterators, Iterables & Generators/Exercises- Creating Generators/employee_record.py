def employee_records():
    employees = [
        {"id": 101, "name": "John", "department": "Python", "salary": 90000},
        {"id": 102, "name": "Jane", "department": "Java", "salary": 80000},
        {"id": 103, "name": "Mike", "department": "Python", "salary": 75000},
        {"id": 104, "name": "Rahul", "department": "Java", "salary": 85000}
    ]

    for employee in employees:
        yield employee

result = employee_records()

for employee in result:
    print(employee)