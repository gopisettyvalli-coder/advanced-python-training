from functools import wraps

def log_function(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling function: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Function {func.__name__} completed")

        return result

    return wrapper

@log_function
def add(a, b):
    return a + b

result = add(10, 20)

print("Result:", result)