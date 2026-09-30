import json

student = {
    "name": "Valli",
    "age": 22,
    "course": "Python"
}

json_data = json.dumps(student)

print(json_data)