print("===== Employee Management System =====")

name = ""
salary = 0
bonus = 0

while True:
    print("\n1. Add Employee")
    print("2. Calculate Salary")
    print("3. Calculate Bonus")
    print("4. Display Employee")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter employee name: ")
        salary = float(input("Enter basic salary: "))
        bonus = 0

        print("Employee added successfully.")

    elif choice == 2:
        if name == "":
            print("Please add employee first.")
        else:
            gross_salary = salary + bonus
            print("Basic Salary:", salary)
            print("Bonus:", bonus)
            print("Gross Salary:", gross_salary)

    elif choice == 3:
        if name == "":
            print("Please add employee first.")
        else:
            if salary >= 50000:
                bonus = salary * 0.20
            elif salary >= 30000:
                bonus = salary * 0.15
            elif salary >= 20000:
                bonus = salary * 0.10
            else:
                bonus = salary * 0.05

            print("Bonus:", bonus)

    elif choice == 4:
        if name == "":
            print("Please add employee first.")
        else:
            print("\n===== Employee Details =====")
            print("Employee Name:", name)
            print("Basic Salary:", salary)
            print("Bonus:", bonus)
            print("Final Salary:", salary + bonus)

    elif choice == 5:
        print("Thank you for using Employee Management System.")
        break

    else:
        print("Invalid choice. Please try again.")