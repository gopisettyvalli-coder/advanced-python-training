import csv

employees = [
    ["ID", "Name", "Department", "Salary"],
    [101, "Ravi", "IT", 30000],
    [102, "Anu", "HR", 28000],
    [103, "Kiran", "Finance", 35000]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

print("Data written to employees.csv")


print("\nReading data from employees.csv:")

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)