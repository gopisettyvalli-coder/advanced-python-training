def decorator(func):
    
     def wrapper():
        print("Before Calling the function")

        func()

        print("After calling the function")

     return wrapper

@decorator
def greet():
    print("Hello Python!")

greet()