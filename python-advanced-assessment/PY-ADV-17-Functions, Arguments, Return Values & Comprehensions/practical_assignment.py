def get_employee_details():
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    salary = float(input("Enter basic salary: "))

    return name, employee_id, salary

def calculate_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross_salary = basic_salary + hra + da

    return gross_salary

def calculate_bonus(basic_salary):
    bonus = basic_salary * 0.10

    return bonus

def calculate_deductions(gross_salary):
    pf = gross_salary * 0.12
    tax = gross_salary * 0.10
    deductions = pf + tax

    return deductions

def calculate_net_salary(gross_salary, bonus, deductions):
    net_salary = gross_salary + bonus - deductions

    return net_salary

def display_salary_slip(name, employee_id, basic_salary, gross_salary, bonus, deductions, net_salary):
    print("\n----- SALARY SLIP -----")
    print("Employee Name:", name)
    print("Employee ID:", employee_id)
    print("Basic Salary:", basic_salary)
    print("Gross Salary:", gross_salary)
    print("Bonus:", bonus)
    print("Deductions:", deductions)
    print("Net Salary:", net_salary)

def main():
    name, employee_id, basic_salary = get_employee_details()

    gross_salary = calculate_salary(basic_salary)

    bonus = calculate_bonus(basic_salary)

    deductions = calculate_deductions(gross_salary)

    net_salary = calculate_net_salary(gross_salary, bonus, deductions)

    display_salary_slip(
        name,
        employee_id,
        basic_salary,
        gross_salary,
        bonus,
        deductions,
        net_salary
    )

main()