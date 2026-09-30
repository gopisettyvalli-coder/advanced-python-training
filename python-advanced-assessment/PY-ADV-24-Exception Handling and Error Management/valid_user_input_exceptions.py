try:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    print("Valid marks:", marks)

except ValueError as e:
    print("Invalid input:", e)