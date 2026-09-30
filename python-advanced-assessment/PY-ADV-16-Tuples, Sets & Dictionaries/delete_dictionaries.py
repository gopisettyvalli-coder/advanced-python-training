student={
    "name": "Valli",
    "age": 22,
    "marks": 85,
    "roll.no": 24
}

print("Student detaiils:", student)

del student["roll.no"]
del student["age"]

print("Updated student details:", student)