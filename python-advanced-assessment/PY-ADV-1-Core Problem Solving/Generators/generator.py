def generate_numbers():
    for i in range(1, 6):
        yield i

for number in generate_numbers():
    print(number)