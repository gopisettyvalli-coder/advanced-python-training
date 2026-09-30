def outer():
    name = "Valli"

    def inner():
        print("Hello", name)

    return inner

greet = outer()
greet()