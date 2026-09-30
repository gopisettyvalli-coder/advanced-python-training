class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id= student_id
        self.name= name
        self.age= age
        self.course= course

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

class StudentManagementSystem: 
    def __init__(self):
        self.students=[]
   
    def add_students(self):
        try:
            student_id=int(input("Enter the student id:"))
            name=input("Enter the name:")
            age=int(input("Enter age:"))
            course=input("Enter course:")
            student=Student(student_id, name, age, course)
            self.students.append(student)
            print("Data added successfully")
        except ValueError:
                    print("Invalid student id, Please enter correct student id")
   
    def display_students(self):
        if not self.students:
            print("Data not found")
        else:
            print("\nStudent Details")
            for student in self.students:
                student.display()
                print("")
        input("\nPress Enter to continue...")

    def search_students(self):
        student_id=int(input("Enter id to search:"))
        for student in self.students:
            if student.student_id==student_id:
                student.display()
                return

        print("Student not found")

    def update_student(self):
        student_id=int(input("Enter student id:"))
        for student in self.students:
            if student.student_id==student_id:
                print("Student found")
                student.display()
                student.name=input("Enter the name:")
                try:
                    student.age=int(input("Enter age:"))
                except ValueError:
                    print("Invalid age, Update canelled")
                    return
                student.course=input("Enter course:")
                print("Student updated successsfully")
                return
        print("Student not found")

    def delete_student(self):
        student_id=int(input("Enter studentid to delete:"))
        for student in self.students:
            if student.student_id==student_id:
                self.students.remove(student)
                print("Students removed sucessfully")
                return
        print("Student not found")

def main():
    system=StudentManagementSystem()
    while True:
        print("\n ====== StudentMAnagement System =====")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Searh Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice=int(input("Enter your choice:"))

        if choice==1:
            system.add_students()
        elif choice==2:
            system.display_students()
        elif choice==3:
            system.search_students()
        elif choice==4:
            system.update_student()
        elif choice==5:
            system.delete_student()
        elif choice==6:
            print("Exiting the program")
            break
        else:
            print("Invalid choice, please try again")
main()                
