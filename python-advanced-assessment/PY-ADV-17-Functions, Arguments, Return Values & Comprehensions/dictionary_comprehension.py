numbers = [1, 2, 3, 4, 5]
squares = {number: number * number for number in numbers}

print(squares)
print()

names = ["Valli", "Ravi", "Sita"]
name_lengths = {name: len(name) for name in names}

print(name_lengths)
