from collections import defaultdict

def generate_report(employees):
    print("\n========== EMPLOYEE REPORT ==========")

    total_salary = 0
    department_count = defaultdict(int)

    for employee in employees:
        bonus = employee["salary"] * (
            0.10 if employee["experience"] >= 5 else 0.05
        )

        total_salary += employee["salary"]
        department_count[employee["department"]] += 1

        print(f"\nEmployee ID : {employee['employee_id']}")
        print(f"Name        : {employee['name']}")
        print(f"Department  : {employee['department']}")
        print(f"Basic Salary: ₹{employee['salary']:.2f}")
        print(f"Bonus       : ₹{bonus:.2f}")
        print(f"Total Salary: ₹{employee['salary'] + bonus:.2f}")

    print("\n========== SUMMARY ==========")
    print(f"Total Employees: {len(employees)}")
    print(f"Total Basic Salary: ₹{total_salary:.2f}")

    print("\nDepartment-wise Employee Count:")

    for department, count in department_count.items():
        print(f"{department}: {count}")