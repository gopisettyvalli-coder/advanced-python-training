from functools import wraps

def validate_age(func):

    @wraps(func)
    def wrapper(age):
        if age < 18:
            print("Invalid age. Age must be 18 or above.")
            return

        return func(age)
    return wrapper

@validate_age
def register(age):
    print("Registration successful!")

register(25)
register(15)