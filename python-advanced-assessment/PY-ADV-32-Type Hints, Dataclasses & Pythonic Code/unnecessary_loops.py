# Unnecessary Loops

nums=[10,20,30,40,50]
total=0

for number in nums:
    total+=number

print("Total:", total)
print()


# Better Version
nums=[10,20,30,40,50]
result=sum(nums)

print(result)