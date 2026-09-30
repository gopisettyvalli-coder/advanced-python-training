import json

data = {
    "name": "Radha",
    "age": 22,
    "course": "Python"
}

with open("sample.json", "w") as file:
    json.dump(data, file)

print("JSON file created successfully")