nums=[10,20,30]

iterator=iter(nums)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Using try-except block to handle StopIteration Exception
nums=[10,20,30,40]

iterator=iter(nums)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

except StopIteration:
    print("StopIteration Exception is raised")