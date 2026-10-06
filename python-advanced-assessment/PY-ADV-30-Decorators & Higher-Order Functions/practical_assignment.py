import time
from functools import wraps
 
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\nFunction Started: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Function Completed: {func.__name__}")
        return result

    return wrapper

def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if func.__name__ == "calculate_salary":
            if len(args) < 2:
                raise ValueError(
                    "Basic salary and bonus are required"
                )

            basic_salary, bonus = args[0], args[1]

            if not isinstance(basic_salary, (int, float)):
                raise ValueError("Basic salary must be numeric")

            if not isinstance(bonus, (int, float)):
                raise ValueError("Bonus must be numeric")

            if basic_salary < 0 or bonus < 0:
                raise ValueError("Salary and bonus cannot be negative")
            
        if func.__name__ == "create_employee":
            name = args[0] if args else kwargs.get("name")

            if not isinstance(name, str) or not name.strip():
                raise ValueError("Employee name cannot be empty")

        print("Input Validation: Successful")

        return func(*args, **kwargs)

    return wrapper

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        elapsed = end_time - start_time

        print(f"Execution Time: {elapsed:.6f} seconds")

        return result

    return wrapper

@log_execution
@validate_input
@measure_time
def create_employee(name, department):
    print(f"Creating employee: {name}")
    print(f"Department: {department}")
    return {"name": name, "department": department}

@log_execution
@validate_input
@measure_time
def calculate_salary(basic_salary, bonus):
    print("Calculating salary...")
    total_salary = basic_salary + bonus
    print(f"Total Salary: ₹{total_salary}")
    return total_salary

@log_execution
@validate_input
@measure_time
def delete_employee(employee_id):
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID must be a positive integer")

    print(f"Employee {employee_id} deleted successfully")

@log_execution
@validate_input
@measure_time
def generate_report(department):
    print(f"Generating report for {department} department")
    print("Report generated successfully")

if __name__ == "__main__":

    employee = create_employee("Valli", "Python")
    print("Employee Details:", employee)

    calculate_salary(30000, 5000)

    delete_employee(101)

    generate_report("Python")