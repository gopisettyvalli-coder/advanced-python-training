from services.employee_service import EmployeeService
from exceptions.employee_exceptions import EmployeeNotFoundException

service = EmployeeService("data.employees.json")

while True:

    print("\nEmployee Management System")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            employee_id = int(input("Enter employee ID: "))
            name = input("Enter name: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))

            service.add_employee(
                employee_id,
                name,
                department,
                salary
            )

        elif choice == "2":

            service.view_employees()

        elif choice == "3":

            employee_id = int(input("Enter employee ID: "))

            service.search_employee(employee_id)

        elif choice == "4":

            employee_id = int(input("Enter employee ID: "))
            name = input("Enter new name: ")
            department = input("Enter new department: ")
            salary = float(input("Enter new salary: "))

            service.update_employee(
                employee_id,
                name,
                department,
                salary
            )

        elif choice == "5":

            employee_id = int(input("Enter employee ID: "))

            service.delete_employee(employee_id)

        elif choice == "6":

            print("Thank you!")
            break

        else:

            print("Invalid choice")

    except EmployeeNotFoundException as e:

        print(e)

    except ValueError as e:

        print(e)