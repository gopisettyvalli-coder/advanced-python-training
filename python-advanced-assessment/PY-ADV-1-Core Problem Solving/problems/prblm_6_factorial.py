num=int(input("Enter a number:"))
factorial=1

for number in range(1,num+1):
    factorial*=number

print("Factorial:", factorial)