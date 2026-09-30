# Singleton Pattern

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Logger created")
        return cls._instance

    def log(self, message):
        print("LOG:", message)


# Factory Pattern
class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


class PaymentFactory:

    @staticmethod
    def create_payment(payment_type):

        if payment_type == "card":
            return CreditCardPayment()

        elif payment_type == "upi":
            return UPIPayment()

        elif payment_type == "cash":
            return CashPayment()

        else:
            raise ValueError("Invalid payment type")


# Main Program
# Testing Singleton

logger1 = Logger()
logger1.log("Application started")

logger2 = Logger()
logger2.log("Payment process started")

print("Same logger object:", logger1 is logger2)


# Testing Factory

payment1 = PaymentFactory.create_payment("card")
payment1.pay(1000)

payment2 = PaymentFactory.create_payment("upi")
payment2.pay(500)

payment3 = PaymentFactory.create_payment("cash")
payment3.pay(200)