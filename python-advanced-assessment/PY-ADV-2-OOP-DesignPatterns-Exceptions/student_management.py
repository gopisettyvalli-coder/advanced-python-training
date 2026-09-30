class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

students = []

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

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100")

        else:
            student = Student(name, age, marks)
            students.append(student)

            print("Student added successfully")

    elif choice == "2":

        if len(students) == 0:
            print("No students found")

        else:
            for student in students:
                student.display()
                print("Grade:", student.calculate_grade())
                print("-------------------")

    elif choice == "3":
        print("Program exited")
        break

    else:
        print("Invalid choice")