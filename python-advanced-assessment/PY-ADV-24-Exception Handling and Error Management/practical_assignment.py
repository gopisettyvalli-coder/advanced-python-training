class InvalidEmployeeIdError(Exception):
    pass

class InvalidSalaryError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

employee_id=int(input("Enter employee id:"))
employee_name=input("Enter employee name:")
age=int(input("Enter your age:"))
email=input("Enter employee email:")
salary=int(input("Enter employee salary:"))
department=input("Enter employee department:")


try:
    if employee_id<=0:
        raise InvalidEmployeeIdError("Invalid Employee ID")
  
    if age<=0:
        raise InvalidAgeError("You must be 18 or above")

    if "@"  not in email:
        raise InvalidEmailError("Invalid Email")

    if salary<=0:
        raise InvalidSalaryError("Salary must be greaater than 0")

    print("Employee validation successful")
    print("Employee Name:", employee_name)
    print("Employee ID:", employee_id)
    print("Age:", age)
    print("Email:", email)
    print("Salary:", salary)
    print("Department:", department)

except InvalidEmployeeIdError as e:
    print(e)

except InvalidSalaryError as e:
    print(e)

except InvalidEmailError as e:
    print(e)

except InvalidAgeError as e:
    print(e)
