def outer():

    def inner():
        print("Python Developer")

    return inner

result=outer()
result()