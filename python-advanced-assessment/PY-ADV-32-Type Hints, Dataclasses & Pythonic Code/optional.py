from typing import Optional

def greet(name: Optional[str])-> str:
    if name is "None":
        return "Hello Guest"
    return "Hello "+ name

print(greet("Rahul"))
print(greet(None))

print()

# Age Optional

from typing import Optional

def check_age(age: Optional[int])-> int:
    if age is None:
        return "Age is not provided"

    return age>=18

print(check_age(22))
print(check_age(None))