print("===== Employee Salary Calculation =====")

name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))

if salary >= 50000:
    bonus = salary * 0.20
elif salary >= 30000:
    bonus = salary * 0.15
elif salary >= 20000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

gross_salary = salary + bonus

tax = gross_salary * 0.10

final_salary = gross_salary - tax

print("\n===== Salary Details =====")
print("Employee Name:", name)
print("Basic Salary:", salary)
print("Bonus:", bonus)
print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Final Salary:", final_salary)