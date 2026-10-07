class EmployeeContext:
    def __enter__(self):
        print("Employee processing started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Employee processing completed")

with EmployeeContext():
    print("Adding employee")
    print("Calculating salary")
    print("Generating report")