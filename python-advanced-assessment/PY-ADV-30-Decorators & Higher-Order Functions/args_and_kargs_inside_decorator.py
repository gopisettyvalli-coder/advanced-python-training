def decorator(func):

    def wrapper(*args, **kwargs):
        print("Function is strating")

        result = func(*args, **kwargs)
        print("Execution completed")

        return result
    return wrapper

@decorator
def add(a,b):
    return a+b

print(add(10,20))


    
