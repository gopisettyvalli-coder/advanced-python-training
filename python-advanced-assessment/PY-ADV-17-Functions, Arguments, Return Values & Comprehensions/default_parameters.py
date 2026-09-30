def greet(name="Valli"):
    print("Hello"  + " "+ name)

greet()
print()

def student(name, age=22):
    print(name)
    print(age)

student("Valli")
print()

def student(name, course="Python"):
    print("Name:", name)
    print("Course:", course)

student("Valli")
student("Ravi", "Java")