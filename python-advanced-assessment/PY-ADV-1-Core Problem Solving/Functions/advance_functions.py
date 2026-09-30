def sub(x,y):
    return x

def calculate(x,y,operation):
    return operation(x,y)

result=calculate(15,6, sub)
print("Result:", result)