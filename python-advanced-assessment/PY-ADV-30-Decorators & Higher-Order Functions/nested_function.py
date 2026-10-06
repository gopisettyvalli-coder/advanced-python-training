def outer():
    print("This is outer function")

    def inner():
        print("This is innner function")

    inner()

outer()


# Second Example

def calculate():
    def add(a,b):
        return a+b

    def subtract(a,b):
        return a-b

    result1=add(10,90)
    result2=subtract(25,16)

    print("Addition:", result1)
    print("Subtraction:", result2)

calculate()