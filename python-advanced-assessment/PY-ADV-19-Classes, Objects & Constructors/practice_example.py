# Student Class
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display_details(self):
        print("Student name:", self.name)
        print("Student age:", self.age)
        print("Student marks:", self.marks)

# Bank Account class
class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance

    def display_details(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)

# Product Class
class ProductClass:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price

    def display_details(self):  
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Price of the product:", self.price)

# Car Class
class Car:
    def __init__(self,car_number,brand,color):
        self.car_number=car_number
        self.brand=brand
        self.color=color
    def display_details(self):
        print("Car Number:", self.car_number)
        print("Car Brand:", self.brand)
        print("Car Color:", self.color)

student=Student("Neethu", 22, 80)
student.display_details()

print()

bank_account=BankAccount(2908474832, "Seetha", 150000)
bank_account.display_details()

print()

product_class=ProductClass(1249575, "Book", 45)
product_class.display_details()

print()

car=Car("AP09B9983", "BMW", "Black")
car.display_details()

