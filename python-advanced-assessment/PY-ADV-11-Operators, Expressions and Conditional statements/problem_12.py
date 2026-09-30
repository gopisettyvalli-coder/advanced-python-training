salary=int(input("Enter your salary:"))
experience=int(input("Enter your experience:"))

if salary>=50000 and experience>=5:
    bonus=salary*0.30
    print("Bonus:", bonus)
elif salary>=30000 and experience>=3:
    bonus=salary*0.20
    print("Bonus:", bonus)
else:
    print("No bonus")