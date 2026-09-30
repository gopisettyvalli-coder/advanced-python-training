number = int(input("Enter a number: "))

if number <= 1:
    print("Not a prime number")
else:
    count = 0

    for i in range(2, number):
        if number % i == 0:
            count = count + 1
            break

    if count == 0:
        print("Prime number")
    else:
        print("Not a prime number")