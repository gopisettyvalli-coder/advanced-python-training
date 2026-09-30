class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

print("Addition:", Calculator.add(10, 20))
print("Subtraction:", Calculator.subtract(20, 10))
print("Multiplication:", Calculator.multiply(5, 4))
print("Division:", Calculator.divide(20, 5))