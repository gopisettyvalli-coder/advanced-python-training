balance=100000

print("===== Banking System =====")
print("1.Check balance")
print("2.Deposit")
print("3.Withdrawl")

choice=int(input("Enter a number(1-3):"))

if choice==1:
    print("Balance:", balance)

elif choice==2:
    amount=float(input("Enter amount to deposit:"))
    balance+=amount
    print("Amount deposited successfully")
    print("Balance:", balance)

elif choice==3:
    amount=float(input("Enter amount to withdrawl:"))

    if amount>balance:
        print("Insufficient balance")

    else:
        balance-=amount
        print("Amount withdrawn successfully")
        print("Balance:", balance)
    
else:
    print("Enter valid choice")