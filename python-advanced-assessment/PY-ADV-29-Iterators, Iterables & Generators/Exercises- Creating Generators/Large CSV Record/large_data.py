import csv

def read_csv_records(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row

result = read_csv_records("employees.csv")

for employee in result:
    print(employee)