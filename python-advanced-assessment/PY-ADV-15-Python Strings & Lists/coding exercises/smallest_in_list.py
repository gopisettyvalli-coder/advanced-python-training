numbers=[12,20,45,30,78,11,5,2]
smallest=numbers[0]

for num in numbers:
    if num<smallest:
        smallest=num

print("Smallest number:", smallest)