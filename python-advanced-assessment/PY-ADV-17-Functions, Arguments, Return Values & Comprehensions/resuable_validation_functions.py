def validate_age(age):
    if age>18:
        return True
    else:
        return False

print(validate_age(20))
print()

def validate_salary(salary):
    if salary>30000:
        return True
    else:
        return False

print(validate_salary(40000))