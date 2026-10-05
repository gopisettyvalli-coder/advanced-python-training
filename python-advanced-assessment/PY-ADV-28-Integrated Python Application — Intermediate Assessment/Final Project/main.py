from services.employee_service import EmployeeService
from storage.employee_storage import EmployeeStorage
from logging_config.logger import get_logger

from exceptions.custom_exceptions import (
    EmployeeManagementError
)


def get_employee_details():

    employee_id = input("Employee ID: ")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    salary = input("Salary: ")
    department = input("Department: ")

    skills_input = input(
        "Skills (comma separated): "
    )

    skills = []

    for skill in skills_input.split(","):

        skill = skill.strip()

        if skill:
            skills.append(skill)

    return (
        employee_id,
        name,
        age,
        email,
        salary,
        department,
        skills
    )


def display_employees(employees):

    if not employees:

        print("\nNo employees found.")

        return

    for employee in employees:

        employee.display()


def main():

    logger = get_logger()

    storage = EmployeeStorage()

    service = EmployeeService(
        storage,
        logger
    )

    print("\n======================================")
    print("     EMPLOYEE MANAGEMENT SYSTEM V4")
    print("======================================")

    while True:

        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Search by Department")
        print("7. Search by Skill")
        print("8. Generate Employee Report")
        print("9. Export Employee Data")
        print("10. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        try:

            # ==================================
            # 1. ADD
            # ==================================

            if choice == "1":

                details = get_employee_details()

                service.add_employee(*details)

                print(
                    "\nEmployee added successfully."
                )

            # ==================================
            # 2. VIEW
            # ==================================

            elif choice == "2":

                print(
                    "\n========== EMPLOYEE LIST =========="
                )

                employees = service.view_employees()

                display_employees(employees)

            # ==================================
            # 3. SEARCH
            # ==================================

            elif choice == "3":

                keyword = input(
                    "Enter employee ID, name or email: "
                )

                results = service.search_employee(
                    keyword
                )

                display_employees(results)

            # ==================================
            # 4. UPDATE
            # ==================================

            elif choice == "4":

                employee_id = input(
                    "Enter Employee ID to update: "
                )

                service.find_employee(
                    employee_id
                )

                print(
                    "\nEnter new employee details:"
                )

                details = get_employee_details()

                service.update_employee(
                    *details
                )

                print(
                    "\nEmployee updated successfully."
                )

            # ==================================
            # 5. DELETE
            # ==================================

            elif choice == "5":

                employee_id = input(
                    "Enter Employee ID to delete: "
                )

                service.delete_employee(
                    employee_id
                )

                print(
                    "\nEmployee deleted successfully."
                )

            # ==================================
            # 6. DEPARTMENT
            # ==================================

            elif choice == "6":

                department = input(
                    "Enter department: "
                )

                results = service.search_department(
                    department
                )

                display_employees(results)

            # ==================================
            # 7. SKILL
            # ==================================

            elif choice == "7":

                skill = input(
                    "Enter skill: "
                )

                results = service.search_skill(
                    skill
                )

                display_employees(results)

            # ==================================
            # 8. REPORT
            # ==================================

            elif choice == "8":

                report = service.generate_report()

                print(
                    "\n========== EMPLOYEE REPORT =========="
                )

                print(
                    "Total Employees:",
                    report["total_employees"]
                )

                print(
                    "Average Salary:",
                    f"{report['average_salary']:.2f}"
                )

                print(
                    "\nEmployees by Department:"
                )

                if report["departments"]:

                    for department, count in (
                        report["departments"].items()
                    ):

                        print(
                            f"{department}: {count}"
                        )

                else:

                    print(
                        "No departments available."
                    )

            # ==================================
            # 9. EXPORT
            # ==================================

            elif choice == "9":

                service.export_data()

                print(
                    "\nEmployee data exported successfully."
                )

            # ==================================
            # 10. EXIT
            # ==================================

            elif choice == "10":

                print(
                    "\nThank you for using "
                    "Employee Management System."
                )

                break

            # ==================================
            # INVALID
            # ==================================

            else:

                print(
                    "\nInvalid choice."
                )

                print(
                    "Please enter a number from 1 to 10."
                )

        except EmployeeManagementError as error:

            print(
                f"\nError: {error}"
            )

            logger.error(
                str(error)
            )

        except Exception as error:

            print(
                f"\nUnexpected error: {error}"
            )

            logger.exception(
                "Unexpected application error"
            )


if __name__ == "__main__":
    main()