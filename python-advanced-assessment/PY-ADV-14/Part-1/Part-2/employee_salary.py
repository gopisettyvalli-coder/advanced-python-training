print("===== EMPLOYEE SALARY MANAGEMENT SYSTEM =====")

name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10

gross_salary = basic_salary + hra + da

if basic_salary >= 50000:
    bonus = basic_salary * 0.20
elif basic_salary >= 30000:
    bonus = basic_salary * 0.15
elif basic_salary >= 20000:
    bonus = basic_salary * 0.10
else:
    bonus = basic_salary * 0.05

if gross_salary >= 50000:
    tax = gross_salary * 0.10
elif gross_salary >= 30000:
    tax = gross_salary * 0.05
else:
    tax = gross_salary * 0.02

final_salary = gross_salary + bonus - tax

print("\n========== SALARY SLIP ==========")
print("Employee Name :", name)
print("Employee ID   :", employee_id)
print("Basic Salary  :", basic_salary)
print("HRA           :", hra)
print("DA            :", da)
print("Gross Salary  :", gross_salary)
print("Bonus         :", bonus)
print("Tax/Deduction :", tax)
print("Final Salary  :", final_salary)
print("=================================")