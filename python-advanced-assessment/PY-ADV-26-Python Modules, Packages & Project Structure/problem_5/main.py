from file_operations import save_employee, load_employees

save_employee("Valli", 50000)

employees = load_employees()

print(employees)