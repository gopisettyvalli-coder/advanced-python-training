from business_logic import calculate_bonus

salary = int(input("Enter employee's salary:"))

bonus = calculate_bonus(salary)

print("Bonus:", bonus)