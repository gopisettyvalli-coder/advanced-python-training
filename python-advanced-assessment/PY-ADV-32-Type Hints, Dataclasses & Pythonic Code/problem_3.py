# STR
def greet(name: str)-> str:
    return "Hello " + name

result=greet("Seetha")
print(result)

# INT
def multiply(a: int, b: int)-> int:
    return a*b

print(multiply(12,13))

# FLOAT
def calculate_price(price: float)-> float:
    return price

print(calculate_price(22.90))

# BOOL
def check_age(age: int)-> int:
    return age>= 18

print(check_age(22))

# LIST
def get_names(name: list)-> list:
    return name

print(get_names(["Vedha", "Seetha", "Ravi"]))

# DICT
def get_employee(employee: dict)-> dict:
    return employee

result=get_employee({
    "name": "Seetha",
    "salary": 80000
})

print(result)