units=int(input("Enter no.of units:"))

if units<=100:
    bill=units*2

elif units<=200:
    bill=(units*2)+((units-100)*3)

elif units<=300:
    bill=(units*2)+(units*3)+((units-200)*5)

else:
    bill=(units*2)+(units*3)+(units*5)+((units-300)*7)

print("Electricity bill:", bill)