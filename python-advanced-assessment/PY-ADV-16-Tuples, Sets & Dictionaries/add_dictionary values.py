# adding single element

student={
    "name": "Raghu",
    "roll.no": 15,
    "age": 22
}

print("Student details:", student)
student["marks"]= 90
print("Student details after adding:", student)

print("=======================================================")

# adding multiple elements
employee={
    "name": "Anu"
}

print("Employee details:", employee)

employee["salary"]=50000
employee["department"]="backend developer"
employee["city"]="Hyderabad"

print("Employee details after adding elements:", employee)