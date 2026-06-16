"""
Topic: Abstraction
Author: Dineshkumar
"""

from abc import ABC, abstractmethod

# ==================================================
# Example 1: Basic Abstraction
# ==================================================

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


print("=== Shape Example ===")

r = Rectangle(10, 5)
c = Circle(7)

print("Rectangle Area:", r.area())
print("Circle Area:", c.area())


# ==================================================
# Example 2: Payment System
# ==================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


print("\n=== Payment Example ===")

payments = [
    CreditCard(),
    UPI()
]

for payment in payments:
    payment.pay(1000)


# ==================================================
# Example 3: Employee Management System
# ==================================================

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee(Employee):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


print("\n=== Employee Example ===")

e1 = FullTimeEmployee(50000)
e2 = PartTimeEmployee(40, 500)

print("Full Time Salary:", e1.calculate_salary())
print("Part Time Salary:", e2.calculate_salary())


# ==================================================
# Example 4: Vehicle System
# ==================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")


print("\n=== Vehicle Example ===")

vehicles = [
    Car(),
    Bike()
]

for vehicle in vehicles:
    vehicle.start()