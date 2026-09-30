print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if choice == 1:
    result = number1 + number2
    print("Result:", result)

elif choice == 2:
    result = number1 - number2
    print("Result:", result)

elif choice == 3:
    result = number1 * number2
    print("Result:", result)

elif choice == 4:
    if number2 != 0:
        result = number1 / number2
        print("Result:", result)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")