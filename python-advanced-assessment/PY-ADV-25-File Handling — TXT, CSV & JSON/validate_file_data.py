import json

try:
    with open("sample.json", "r") as file:
        data = json.load(file)

    if "name" in data and "age" in data and "course" in data:
        print("File data is valid")
    else:
        print("Required data is missing")

except json.JSONDecodeError:
    print("Invalid JSON format")

except FileNotFoundError:
    print("File not found")