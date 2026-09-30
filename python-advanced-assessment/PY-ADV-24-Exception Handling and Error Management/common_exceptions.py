#Value Error
age=int("abc")

#Type Error
sum= "10" + 5

# Index Error
items=[10, 20, 30, 40]
print(items[5])

# Key-Pair Error
details={"name" : "valli", "age" : "22", "domain" : "Python"}
print(details["salary"])

# Zero Division Error
print(10/0)

# File not found Error
file=open("abc.txt", "r")