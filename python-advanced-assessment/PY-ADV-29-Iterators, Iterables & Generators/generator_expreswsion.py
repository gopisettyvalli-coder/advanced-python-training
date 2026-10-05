numbers = [10, 20, 30, 40, 50]

generator = (x * 2 for x in numbers)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))