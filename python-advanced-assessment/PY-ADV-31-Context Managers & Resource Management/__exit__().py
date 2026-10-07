class MyContext:
    def __enter__(self):
        print("Context started")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Context ended")

with MyContext():
    print("Doing some work")