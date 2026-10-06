def outer(x):

    def inner():
        print(x)

    return inner

result = outer(10)

result()