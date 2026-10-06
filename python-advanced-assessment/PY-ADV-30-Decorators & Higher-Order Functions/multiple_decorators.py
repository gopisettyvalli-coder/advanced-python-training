from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function completed")
        return result

    return wrapper

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper

@log
@uppercase
def greet():
    return "hello"

print(greet())