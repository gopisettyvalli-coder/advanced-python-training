import timeit

code_loop = """
total = 0
for i in range(100000):
    total += i
"""

code_sum = """
total = sum(range(100000))
"""

time_loop = timeit.timeit(code_loop, number=100)
time_sum = timeit.timeit(code_sum, number=100)

print("Loop addition time:", round(time_loop, 4), "seconds")
print("Built-in sum time:", round(time_sum, 4), "seconds")