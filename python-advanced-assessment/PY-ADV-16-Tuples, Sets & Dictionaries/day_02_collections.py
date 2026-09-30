# tuple creation

fruits=("apple", "banana", "watermelon")
print(fruits)
print("==========================================")

# accessing by indexing

numbers=(10,20,30,40,25,97)

print(numbers[0])
print(numbers[2])
print(numbers[4])

# negative indexing
print(numbers[-2])
print(numbers[-3])
print(numbers[-1])
print("====================================================")

# length of the tuple

nums=(10,20,30,25,45)

print(len(nums))
print("====================================================")


# checking num in tuple
num=(25,12,39,45,89,20,80)
i=int(input("Enter number to find:"))

if i in num:
    print("Num", i, "exists")

else:
    print("Num", i, "not exists")
