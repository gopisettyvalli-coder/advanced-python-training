class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


class StudentRepository:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return self.students


repository = StudentRepository()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        student = Student(name, age, marks)

        repository.add_student(student)

        print("Student added successfully")

    elif choice == "2":

        students = repository.get_all_students()

        if len(students) == 0:
            print("No students found")

        else:
            for student in students:
                print("Name:", student.name)
                print("Age:", student.age)
                print("Marks:", student.marks)
                print("-------------------")

    elif choice == "3":

        print("Program exited")
        break

    else:
        print("Invalid choice")