def transform_department(department):
    return department.upper()

def calculate_annual_salary(salary):
    return salary * 12

def transform_employee(employee):
    employee["department"] = transform_department(employee["department"])
    employee["annual_salary"] = calculate_annual_salary(employee["salary"])
    return employee

employees = [
    {
        "name": "Ravi",
        "department": "it",
        "salary": 30000
    },
    {
        "name": "Anu",
        "department": "hr",
        "salary": 28000
    }
]

transformed_employees = []

for employee in employees:
    transformed_employees.append(transform_employee(employee))
print("Transformed Employee Data:")

for employee in transformed_employees:
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Monthly Salary:", employee["salary"])
    print("Annual Salary:", employee["annual_salary"])
    print()