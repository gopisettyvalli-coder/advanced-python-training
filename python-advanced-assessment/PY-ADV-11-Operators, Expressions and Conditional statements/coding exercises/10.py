print("=========== Electricity Bill Calaculator ===========")

units=int(input("Enter the units:"))

if units<=100:
    bill=units*1.50
    print("Amount:", bill)

elif units<=200:
    bill=units*3.50
    print("Amount:", bill)

elif units<=300:
    bill=units*4.00
    print("Amount:", bill)

else:
    bill=units*5.40
    print("Amount:", bill)