number = input("Enter a number: ")
reverse = number[::-1]

if number == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")