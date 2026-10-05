def fibonacci_series(n):
    a,b=0,1

    for i in range(n):
        yield a
        a,b=b,a+b

result=fibonacci_series(15)

for i in result:
    print(i)
