def odd_numbers():

    for i in range(1,16):
        if i % 2 !=0:
            yield i

result=odd_numbers()

for i in result:
    print(i)