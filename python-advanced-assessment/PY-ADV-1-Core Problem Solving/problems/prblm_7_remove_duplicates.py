numbers=[1,2,3,5,12,2,3,1,90,66,45,1,45]
new_number=[]

for num in numbers:
    if num not in new_number:
        new_number.append(num)

print("New number list:", new_number)