number=[19,21,11,15,90,78,56]
largest=number[0]

for num in number:
    if num > largest:
        largest=num

print("Largest Number:", largest)