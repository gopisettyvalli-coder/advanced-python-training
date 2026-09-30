salary = float(input("Enter basic salary: "))

if salary >= 50000:
    bonus = salary * 0.20
elif salary >= 30000:
    bonus = salary * 0.15
elif salary >= 20000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

final_salary = salary + bonus

print("Basic Salary =", salary)
print("Bonus =", bonus)
print("Final Salary =", final_salary)