import time
from functools import wraps

def calculate_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print(f"{func.__name__} took {execution_time:.4f} seconds")

        return result

    return wrapper

@calculate_time
def calculate_sum():
    total = 0

    for i in range(1000000):
        total += i

    return total

print(calculate_sum())