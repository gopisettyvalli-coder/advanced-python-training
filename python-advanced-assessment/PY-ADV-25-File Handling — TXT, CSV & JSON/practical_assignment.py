import json
import csv
import os

if not os.path.exists("data"):
    os.makedirs("data")

def validate_employee(employee):
    if employee["id"] <= 0:
        print("Invalid employee ID")
        return False

    if employee["age"] < 18:
        print("Invalid age")
        return False

    if employee["salary"] <= 0:
        print("Invalid salary")
        return False

    if employee["name"] == "":
        print("Name cannot be empty")
        return False

    return True

def save_employee(employee):

    with open("data/employees.json", "w") as file:
        json.dump(employee, file, indent=4)

    with open("data/employees.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "name", "age", "department", "salary"]
        )

        writer.writeheader()
        writer.writerow(employee)

    with open("data/employees.txt", "w") as file:
        file.write(str(employee))

    print("Employee saved successfully")

def load_employees():

    with open("data/employees.json", "r") as file:
        employee = json.load(file)

    return employee

def search_employee(employee_id):

    employee = load_employees()

    if employee["id"] == employee_id:
        print("Employee found")
        print(employee)
    else:
        print("Employee not found")

def update_employee(employee_id, new_salary):

    employee = load_employees()

    if employee["id"] == employee_id:
        employee["salary"] = new_salary
        save_employee(employee)
        print("Employee updated successfully")
    else:
        print("Employee not found")

def delete_employee(employee_id):

    employee = load_employees()

    if employee["id"] == employee_id:

        os.remove("data/employees.json")
        os.remove("data/employees.csv")
        os.remove("data/employees.txt")

        print("Employee deleted successfully")

    else:
        print("Employee not found")

employee = {
    "id": 101,
    "name": "Seetha",
    "age": 22,
    "department": "Python",
    "salary": 70000
}

if validate_employee(employee):
    save_employee(employee)

print()

print("Reading employee:")
print(load_employees())

print()

print("Searching employee:")
search_employee(101)

print()

print("Updating employee:")
update_employee(101, 75000)

print()

print("Deleting employee:")
delete_employee(101)