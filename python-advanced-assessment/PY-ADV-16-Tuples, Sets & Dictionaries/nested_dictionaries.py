# nested dictionary
employees={
    "emp 1":{
        "name":"Seetha",
        "salary": 70000,
        "domain": "Python"
    },
    "emp 2" :{
        "name": "Ravi",
        "salary": 50000,
        "domain":" Devops"
    }
}

print(employees["emp 1"]["name"])
print(employees["emp 2"]["salary"])
print(employees["emp 2"]["domain"])


employees["emp 1"]["salary"]= 900000

print(employees)