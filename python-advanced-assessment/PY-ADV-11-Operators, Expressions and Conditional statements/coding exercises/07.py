salary=int(input("Enter your salary:"))
experience=int(input("Enter your experience:"))

if salary>50000 and experience>=5:
    bonus=salary*20/100
    print("Bonus:", bonus)

elif salary>30000 and experience>=3:
    bonus=salary*10/100
    print("Bonus:", bonus)

else:
    bonus=salary*5/100
    print("Bonus:", bonus)

    