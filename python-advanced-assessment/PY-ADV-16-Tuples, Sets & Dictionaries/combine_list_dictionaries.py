# list of dictionaries

employees=[
    {"name": "valli", "age": 22, "salary": 85000},
    {"name": "Seetha", "age":23, "salary": 90000},
    {"name": "Aravind", "age": 20, "salary":80000}
]

print(employees)
print(employees[0]["name"])
print(employees[1]["salary"])
print("==============================================")

for employee in employees:
    print(employee["name"]), (employee["salary"])
print("==============================================")

# dictionary containing list 

student={
    "name": "Seetha",
    "roll.no": 26,
}
skills= ["Python", "SQL", "API"]
print(student)
student["skills"]=skills
print(student)