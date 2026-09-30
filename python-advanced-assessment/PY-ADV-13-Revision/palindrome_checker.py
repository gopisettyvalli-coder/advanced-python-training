number = int(input("Enter a number: "))
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")