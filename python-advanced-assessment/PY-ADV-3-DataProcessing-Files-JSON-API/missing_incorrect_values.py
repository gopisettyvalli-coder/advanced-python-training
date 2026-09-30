def validate_marks(marks):

    if marks is None:
        print("Marks are missing")
        return False

    if not isinstance(marks, (int, float)):
        print("Marks must be a number")
        return False

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
        return False

    return True

marks = int(input("Enter marks:"))

if validate_marks(marks):
    print("Valid marks")
else:
    print("Invalid marks")