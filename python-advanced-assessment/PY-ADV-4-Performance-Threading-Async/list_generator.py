import sys

is_active = True
ratio = 3.14159
user_tuple = ("admin", "editor", "viewer")
user_dict = {"id": 101, "role": "admin"}

print("Memory used by boolean:", sys.getsizeof(is_active), "bytes")
print("Memory used by float:", sys.getsizeof(ratio), "bytes")
print("Memory used by tuple:", sys.getsizeof(user_tuple), "bytes")
print("Memory used by dict:", sys.getsizeof(user_dict), "bytes")