age = int(input("Enter age:"))

try:
    if age < 18:
        raise ValueError("Age is too small")

except ValueError as e:
    print(e)