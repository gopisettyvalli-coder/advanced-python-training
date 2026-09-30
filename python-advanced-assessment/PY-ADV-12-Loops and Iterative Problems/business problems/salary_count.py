salary=[30000, 35000, 32000, 40000, 25000, 50000]
count=0

for salaries in salary:
    if salaries>=35000:
        count+=1

print("Employees:", count)