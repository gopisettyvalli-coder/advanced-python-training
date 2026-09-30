numbers=[10,20,30,40,10,20,15,60,40]
nums=[]

for num in numbers:
    if num not in nums:
        nums.append(num)

print("List without duplicates:", nums)