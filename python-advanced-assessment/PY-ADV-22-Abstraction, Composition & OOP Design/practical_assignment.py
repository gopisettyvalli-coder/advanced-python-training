from abc import ABC, abstractmethod

class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.phone=phone

class Account(ABC):
    def __init__(self, account_number, customer, balance):
        self.account_number=account_number
        self.customer=customer
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        print("Amount deposited:", amount)

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def calculate_interest(self):
        interest = self.balance * 0.04
        print("Savings interest:", interest)

class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance + 10000:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Withdrawal limit exceeded")

    def calculate_interest(self):
        print("Current account has no interest")

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def display_customers(self):
        for customer in self.customers:
            print(customer.customer_id, customer.name, customer.email, customer.phone)

    def display_accounts(self):
        for account in self.accounts:
            print(account.account_number, account.customer.name, account.balance)


customer1 = Customer(101, "Seetha", "seetha@gmail.com", "9876543210")

savings = SavingsAccount(1001, customer1, 50000)
current = CurrentAccount(1002, customer1, 30000)

bank = Bank("ABC Bank")

bank.add_customer(customer1)
bank.add_account(savings)
bank.add_account(current)

bank.display_customers()
bank.display_accounts()

savings.deposit(5000)
savings.withdraw(10000)
savings.calculate_interest()

current.deposit(5000)
current.withdraw(35000)
current.calculate_interest()
