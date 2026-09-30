number=int(input("Enter the number:"))

if number>0:
    if number%2==0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("Enter positive number")

print("========================================")

marks=int(input("Enter your marks:"))
attendence=int(input("Enter attendence percentage:"))

if marks>60:
    if attendence>70:
        print("You are eligible for exam")
    else:
        print("You are not eligible")

