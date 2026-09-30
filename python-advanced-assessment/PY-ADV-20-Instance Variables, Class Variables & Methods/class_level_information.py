class Student:
    school_name="Navvena Vidyaniketan School"

    def __init__(self,name,age):
        self.name=name
        self.age=age

student1=Student("Siva", 22)
student2=Student("Shreeya", 23)

print(student1.name)
print(student1.school_name)

print()

print(student2.name)
print(student2.school_name)