from models import Developer, Manager
from services import EmployeeStorage, EmployeeService
from exceptions import InvalidEmployeeError

def main():
    storage = EmployeeStorage()
    service = EmployeeService(storage)

    try:
        developer = Developer(
            101,
            "Seetha",
            25,
            "seetha@gmail.com",
            "Python"
        )

        manager = Manager(
            102,
            "Radha",
            30,
            "radha@gmail.com",
            5
        )

        print(service.add_employee(developer))
        print(service.add_employee(manager))

        print("\nEmployee Details:")

        for employee in service.get_all_employees():
            print(employee.display_details())

        print("\nSearching for employee 101:")
        result = service.get_employee(101)

        if result:
            print(result.display_details())
        else:
            print("Employee not found")

    except InvalidEmployeeError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()