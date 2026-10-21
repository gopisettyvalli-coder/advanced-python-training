from services import EmployeeStorage
from exceptions import InvalidEmployeeError
from models import Developer

def main():
    storage = EmployeeStorage()

    try:
        employee1 = Developer(
            101,
            "Seetha",
            25,
            "seetha@example.com",
            "Python"
        )

        employee2 = Developer(
            102,
            "Radha",
            28,
            "radha@example.com",
            "Java"
        )

# Add employees
        storage.add(employee1)
        storage.add(employee2)

        print("Employees added successfully!")

# Display all employees
        print("\nEmployee Details:")
        for employee in storage.get_all():
            print(employee)

# Test duplicate employee ID
        print("\nTesting duplicate employee ID:")
        try:
            storage.add(employee1)
        except InvalidEmployeeError as error:
            print("Error:", error)

# Test empty storage
        empty_storage = EmployeeStorage()
        print("\nEmpty storage:", empty_storage.get_all())

    except InvalidEmployeeError as error:
        print("Employee error:", error)

if __name__ == "__main__":
    main()
