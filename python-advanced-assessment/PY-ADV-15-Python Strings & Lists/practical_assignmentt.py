employee_name=input("Enter employee full name:")
department=input("Enter department of employee:")
email=input("Enter employee mail-id:")

employee_names=employee_name.strip().split()
first_name=employee_names[0]
last_name=employee_names[-1]

formatted_name=first_name.title() + " "+ last_name.title()
email_username=email.split("@")[0]

print("First Name:", first_name)
print("Last Name:", last_name)
print("Email Id:", email_username)
print("Department:", department)

