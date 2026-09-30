import json

data = '''
{
    "name": "Ravi",
    "age": 25,
    "salary": 30000
}
'''

employee = json.loads(data)

employee["name"] = employee["name"].upper()
employee["salary"] = employee["salary"] + 5000

print("Name:", employee["name"])
print("Age:", employee["age"])
print("Updated Salary:", employee["salary"])