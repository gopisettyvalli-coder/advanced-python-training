def add(*args):
    print(args)

add(10,29)
add(10,20,30)
print()

def add(*args):
    total = 0

    for number in args:
        total = total + number

    return total

print(add(10, 20))
print(add(10, 20, 30, 40))




