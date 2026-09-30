employees = {
    101: {
        "name": "Vedha",
        "department": "IT",
        "salary": 85000,
        "skills": ["Python", "SQL"],
        "experience": 2
    },

    102: {
        "name": "Aravind",
        "department": "HR",
        "salary": 60000,
        "skills": ["Excel", "Communication"],
        "experience": 3
    },

    103: {
        "name": "Seetha",
        "department": "IT",
        "salary": 90000,
        "skills": ["Python", "Django"],
        "experience": 4
    },

    104: {
        "name": "Rahul",
        "department": "Finance",
        "salary": 75000,
        "skills": ["Excel", "SQL"],
        "experience": 3
    },

    105: {
        "name": "Priya",
        "department": "IT",
        "salary": 70000,
        "skills": ["Python", "HTML"],
        "experience": 2
    }
}

# Display all employees
print("\nALL EMPLOYEES")

for employee_id, employee in employees.items():
    print("ID:", employee_id)
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Salary:", employee["salary"])
    print("Skills:", employee["skills"])
    print("Experience:", employee["experience"])
    print()

# Search employee by ID
search_id = int(input("Enter ID to search: "))

if search_id in employees:
    print("\nEmployee Found!")
    print("ID:", search_id)
    print("Name:", employees[search_id]["name"])
    print("Department:", employees[search_id]["department"])
    print("Salary:", employees[search_id]["salary"])
else:
    print("Employee not found")

# Search employee by department
search_department = input("\nEnter department to search: ")

print("\nEMPLOYEES IN", search_department.upper())

for employee_id, employee in employees.items():
    if employee["department"].lower() == search_department.lower():
        print(employee_id, employee["name"])

# Find highest salary
highest_salary = 0
highest_employee = ""

for employee_id, employee in employees.items():
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        highest_employee = employee["name"]

print("\nHIGHEST SALARY")
print("Employee:", highest_employee)
print("Salary:", highest_salary)

# Find lowest salary
lowest_salary = float("inf")
lowest_employee = ""

for employee_id, employee in employees.items():
    if employee["salary"] < lowest_salary:
        lowest_salary = employee["salary"]
        lowest_employee = employee["name"]

print("\nLOWEST SALARY")
print("Employee:", lowest_employee)
print("Salary:", lowest_salary)

# Display employees by skill
search_skill = input("\nEnter skill to search: ")

print("\nEMPLOYEES WITH", search_skill.upper(), "SKILL")

for employee_id, employee in employees.items():
    for skill in employee["skills"]:
        if skill.lower() == search_skill.lower():
            print(employee_id, employee["name"])