balance=100000
withdrawl=float(input("Enter amount to withdrawl:"))

if withdrawl > balance:
    print("Insufficient balance")

else:
    balance-=withdrawl
    print("Amount withdrawn successfully", withdrawl)
    print("B?alance Amount:", balance)