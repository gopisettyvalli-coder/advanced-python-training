# import complete module
import math
print(math.sqrt(16))

# import specific function
from math import sqrt
print(sqrt(25))

# import multiple functions
from math import sqrt, factorial
print(sqrt(36))
print(factorial(5))

# using module as alias
import math as m
print(m.sqrt(49))