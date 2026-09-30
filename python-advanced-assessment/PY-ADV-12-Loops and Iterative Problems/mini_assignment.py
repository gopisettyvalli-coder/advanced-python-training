print("=========== Student MArks Processing Program ==========")

student=int(input("Enter no.of students:"))
for i in range(1, student + 1):

    print("\nStudent", i)

    marks = []

    for j in range(1, 4):
        mark = float(input(f"Enter marks for subject {j}: "))

        while mark < 0 or mark > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            mark = float(input(f"Enter marks for subject {j} again: "))

        marks.append(mark)
    total = sum(marks)

    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 50:
        grade = "E"
    else:
        grade = "F"

    print("\n----- Result -----")
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)