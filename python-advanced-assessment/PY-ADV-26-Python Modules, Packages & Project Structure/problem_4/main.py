from validation_logic import validate_salary

salary = 50000

if validate_salary(salary):
    print("Valid salary")
else:
    print("Invalid salary")