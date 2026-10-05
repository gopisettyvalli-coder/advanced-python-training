def employees():
    for i in range(1, 1000001):
        yield f"Employee {i}"

for employee in employees():
    print(employee)