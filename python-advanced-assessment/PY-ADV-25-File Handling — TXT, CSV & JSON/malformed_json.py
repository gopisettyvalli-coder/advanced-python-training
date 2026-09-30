import json

data = '{"name": "Valli", "age": 22'

try:
    student = json.loads(data)
    print(student)
except json.JSONDecodeError:
    print("Invalid JSON data")