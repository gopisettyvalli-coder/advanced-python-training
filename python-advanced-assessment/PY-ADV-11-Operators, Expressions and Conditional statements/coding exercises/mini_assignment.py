employee_name=input("Enter name of the employee:")
salary=float(input("Enter the salary:"))
rating=int(input("Enter the rating:"))
experience=int(input("Enter experience:"))

if rating<1 and experience>5:
    print("Enter valid numbers from 1-5")

elif rating>=5 and experience>=5:
    bonus=salary*0.20
    print("Bonus:", bonus)

elif rating>=4 and experience>=3:
    bonus=salary*0.15
    print("Bonus:", bonus)

elif rating>=3 and experience>=2:
    bonus=salary*0.10
    print("Bonus:", bonus)

else:
    bonus=salary*0.05
    print("Bonus:", bonus)

