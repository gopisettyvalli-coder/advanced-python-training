def numbers():
    yield 10
    yield 20
    yield 30

result=numbers()
print(result)

print(next(result))
print(next(result))
print(next(result))