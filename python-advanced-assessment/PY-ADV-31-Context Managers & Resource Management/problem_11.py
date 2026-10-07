# Manual Resource Handling
file=open("sample.txt", "r")

try:
    data=file.read()
    result=10/0

finally:
    file.close()


# Context Managers
with open("sample.txt", "r") as file:
    data = file.read()
    result = 10 / 0