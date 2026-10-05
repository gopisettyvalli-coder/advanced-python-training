def salary_records():
    employees = [
        {"name": "John", "salary": 90000},
        {"name": "Jane", "salary": 80000},
        {"name": "Mike", "salary": 75000},
        {"name": "Rahul", "salary": 85000}
    ]

    for employee in employees:
        if employee["salary"] > 80000:
            yield employee

result = salary_records()

for employee in result:
    print(employee)