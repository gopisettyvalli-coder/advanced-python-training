class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

student1 = Student("Valli", 22)
student2 = Student("Ravi", 23)
student3 = Student("Anu", 21)

print(student1)
print(student2)
print(student3)