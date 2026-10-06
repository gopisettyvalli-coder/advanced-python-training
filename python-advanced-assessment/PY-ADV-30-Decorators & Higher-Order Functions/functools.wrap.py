from functools import wraps

def decorator(func):
      @wraps(func)
   
      def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

      return wrapper

@decorator
def greet(name):
      '''This function is used to greet the person'''
      print("Hello", name)


print(greet.__name__)
print(greet.__doc__)