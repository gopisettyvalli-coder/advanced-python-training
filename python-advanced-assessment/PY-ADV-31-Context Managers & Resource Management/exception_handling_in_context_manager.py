class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("Exception occurred:", exc_value)
            return True   # Suppresses the exception

        print("No exception occurred")
        return False

with MyContext():
    print("Inside context")
    result = 10 / 0

print("Program continues")