def save_employee(name, salary):
    with open("employees.txt", "a") as file:
        file.write(name + "," + str(salary) + "\n")


def load_employees():
    with open("employees.txt", "r") as file:
        data = file.read()
        return data