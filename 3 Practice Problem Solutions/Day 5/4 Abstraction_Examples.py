"""
Topic: Abstraction
Author: Dineshkumar
"""

from abc import ABC, abstractmethod

# ==================================================
# Example 1: Payment Gateway
# ==================================================

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentGateway):

    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card")


class UPI(PaymentGateway):

    def pay(self, amount):
        print(f"₹{amount} paid using UPI")


class NetBanking(PaymentGateway):

    def pay(self, amount):
        print(f"₹{amount} paid using Net Banking")


print("=== Payment Gateway ===")

payments = [
    CreditCard(),
    UPI(),
    NetBanking()
]

for payment in payments:
    payment.pay(1000)


# ==================================================
# Example 2: Notification System
# ==================================================

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print("Email:", message)


class SMSNotification(Notification):

    def send(self, message):
        print("SMS:", message)


class PushNotification(Notification):

    def send(self, message):
        print("Push:", message)


print("\n=== Notification System ===")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send("Welcome User")