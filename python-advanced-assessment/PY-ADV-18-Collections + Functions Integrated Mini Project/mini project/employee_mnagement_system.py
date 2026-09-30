# Employee Management System

print("===============================================")
print()
print("EMPLOYEE MANAGEMENT SYSTEM")
print()
print("===============================================")

employees = [
    {
        "id": 101,
        "name": "Seetha",
        "department": "Python",
        "salary": 70000,
        "skills": {"Python", "SQL"}
    },
    {
        "id": 102,
        "name": "Radha",
        "department": "Java",
        "salary": 80000,
        "skills": {"Java", "OOP"}
    }
]

# Adding employee
def add_employee():
    emp_id = int(input("Enter employee ID: "))
    emp_name = input("Enter employee name: ")
    emp_dept = input("Enter employee department: ")
    emp_salary = float(input("Enter employee salary: "))

    emp_skills = {
        skill.strip()
        for skill in input("Enter employee skills (comma-separated): ").split(",")
        if skill.strip()
    }

    employee = {
        "id": emp_id,
        "name": emp_name,
        "department": emp_dept,
        "salary": emp_salary,
        "skills": emp_skills
    }

    employees.append(employee)

    print("Employee added successfully!")

# View employees
def view_employee():
    if not employees:
        print("No employees found!")
        return

    for employee in employees:
        print("\nEmployee ID:", employee["id"])
        print("Name:", employee["name"])
        print("Department:", employee["department"])
        print("Salary:", employee["salary"])
        print("Skills:", employee["skills"])

# Search employee
def search_employee():
    emp_id = int(input("Enter employee ID to search: "))

    for employee in employees:
        if employee["id"] == emp_id:
            print("\nEmployee found!")
            print("Employee ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            print("Skills:", employee["skills"])
            return

    print("Employee not found!")

# Update employee
def update_employee():
    emp_id = int(input("Enter employee ID to update: "))

    for employee in employees:
        if employee["id"] == emp_id:
            employee["name"] = input("Enter employee name: ")
            employee["department"] = input("Enter employee department: ")
            employee["salary"] = float(input("Enter employee salary: "))

            skills = input("Enter employee skills: ")

            employee["skills"] = {
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            }

            print("Employee updated successfully!")
            return

    print("Employee not found!")

# Delete employee
def delete_employee():
    emp_id = int(input("Enter employee ID: "))

    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)

            print("Employee deleted successfully!")
            return

    print("Employee not found!")

# Search by department
def search_by_department():
    department = input("Enter department: ")
    found = False

    for employee in employees:
        if employee["department"].lower() == department.lower():
            print("\nEmployee ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            print("Skills:", employee["skills"])

            found = True

    if not found:
        print("No employees found in this department.")

# Find highest salary
def highest_salary():
    if not employees:
        print("No employees found!")
        return

    highest = employees[0]

    for employee in employees:
        if employee["salary"] > highest["salary"]:
            highest = employee

    print("\nEmployee with highest salary:")
    print("Employee ID:", highest["id"])
    print("Name:", highest["name"])
    print("Department:", highest["department"])
    print("Salary:", highest["salary"])
    print("Skills:", highest["skills"])

# Search by skill
def search_by_skill():
    skill = input("Enter skill: ").strip().lower()
    found = False

    for employee in employees:
        skills = {s.strip().lower() for s in employee["skills"]}

        if skill in skills:
            print("\nEmployee ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            print("Skills:", employee["skills"])

            found = True

    if not found:
        print("No employees found with this skill.")

# Employee summary
def employee_summary():
    if not employees:
        print("No employees found.")
        return

    total_employees = len(employees)
    total_salary = sum(employee["salary"] for employee in employees)
    average_salary = total_salary / total_employees

    departments = set()
    all_skills = set()

    for employee in employees:
        departments.add(employee["department"])
        all_skills.update(employee["skills"])

    summary = (
        total_employees,
        total_salary,
        average_salary,
        departments,
        all_skills
    )

    print("\n========== EMPLOYEE SUMMARY ==========")
    print("Total Employees:", summary[0])
    print("Total Salary:", summary[1])
    print("Average Salary:", summary[2])
    print("Departments:", summary[3])
    print("All Skills:", summary[4])

while True:
    print("\n1. Add employee")
    print("2. View employees")
    print("3. Search employee")
    print("4. Update employee")
    print("5. Delete employee")
    print("6. Search by department")
    print("7. Find highest salary")
    print("8. Search by skill")
    print("9. Generate employee summary")
    print("10. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employee()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        search_by_department()

    elif choice == "7":
        highest_salary()

    elif choice == "8":
        search_by_skill()

    elif choice == "9":
        employee_summary()

    elif choice == "10":
        print("Thank you for choosing Employee Management System.")
        break

    else:
        print("Invalid choice. Please try again.")