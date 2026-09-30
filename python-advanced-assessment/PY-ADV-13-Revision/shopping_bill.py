print("====== Shopping bill Calaculation =======")

item=input("Enter item name:")
price=int(input("Enter price of item:"))
quantity=int(input("Enter the quantity of an item:"))

total= price*quantity

if price >=5000:
    discount=total*0.20

elif price >=3000:
    discount=total*0.15

elif price >=1000:
    discount=total*0.10

else:
    discount=0

final_amount = total - discount

print("Item:", item)
print("Total Amount:", total)
print("Discount:", discount)
print("Final Bill:", final_amount)