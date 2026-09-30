def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])

student(name="Valli", age=22)
print()


def validate_salary(salary):
    if salary > 0:
        return True
    else:
        return False

print(validate_salary(50000))