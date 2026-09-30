class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Rahul", 20)
student2 = Student("Priya", 18)

student1.display()
student2.display()