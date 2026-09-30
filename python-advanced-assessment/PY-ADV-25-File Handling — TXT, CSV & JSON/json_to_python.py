import json

json_data = '{"name": "Valli", "age": 22, "course": "Python"}'

student = json.loads(json_data)

print(student)
print(student["name"])