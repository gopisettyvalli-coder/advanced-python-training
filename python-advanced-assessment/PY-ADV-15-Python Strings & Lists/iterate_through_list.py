nums=[10,20,30,40]
for i in nums:
    print(i)
print("==============================")


numbers=[10,12,14,20,13,59,60,78]
for num in numbers:
    if num%2==0:
        print(num)
print("==============================")



numbers=[10,12,14,20,13,59,60,78]
count=0
for num in numbers:
    if num%2==0:
        count+=1
print("No.of even numbers:", count)