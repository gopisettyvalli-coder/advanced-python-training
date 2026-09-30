def numbers():
    for i in range(1, 6):
        print("Calculating:", i)
        yield i

nums = numbers()

print(next(nums))
print(next(nums))