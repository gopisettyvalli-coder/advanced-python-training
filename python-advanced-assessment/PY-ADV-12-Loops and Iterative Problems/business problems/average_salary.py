salaries=[20000, 30000, 25000, 13000, 34000]

count=0
sum=0
for salary in salaries:
    count+=1
    sum+=salary

print("Average:", sum/count)
print("Employees:", count)
print("Salary average", sum)