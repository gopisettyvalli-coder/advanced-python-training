import json

def load_employees(filename):

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_employees(filename, employees):

    with open(filename, "w") as file:
        json.dump(employees, file, indent=4)