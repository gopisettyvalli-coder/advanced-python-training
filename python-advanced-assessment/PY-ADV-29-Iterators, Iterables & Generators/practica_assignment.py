def generate_employee():
    employees=[
        {"id": 101, "name": "John", "department": "Python", "salary": 90000},
        {"id": 102, "name": "Jane", "department": "Java", "salary": 80000},
        {"id": 103, "name": "Mike", "department": "JavaScript", "salary": 75000},
        {"id": 104, "name": "Rahul", "department": "C++", "salary": 850000},
        {"id": 105, "name": "Priya", "department": "Python", "salary": 95000},
    ]

    for employee in employees:
        yield employee

def generate_salary_record(employees):
   
    for employee in employees:
        yield{
        "name" : employee["name"],
        "salary" : employee["salary"]
        }

def generate_department_record(employees):
   
    for employee in employees:
        yield{
            "name" : employee["name"],
            "department" : employee["department"]
        }

employee=generate_employee()
print("Employee Records")
for record in employee:
    print(record)

print()
employee=generate_employee()
print("Salary Record:")
for record in generate_salary_record(employee):
    print(record)

print()


employee=generate_employee()
print("Department Records")
for record in generate_department_record(employee):
    print(record)