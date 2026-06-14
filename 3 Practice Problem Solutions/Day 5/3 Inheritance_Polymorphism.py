"""
Inheritance & Polymorphism
"""

# Person -> Student

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        print(self.name, self.roll_no)


s = Student("John", 101)

print("Student")
s.display()


# Vehicle -> Car

class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Car Driving")


car = Car()

print("\nVehicle")
car.start()
car.drive()


# Shape Hierarchy

class Shape:

    def area(self):
        print("Area Calculation")


class Rectangle(Shape):

    def area(self):
        print("Rectangle Area")


class Circle(Shape):

    def area(self):
        print("Circle Area")


print("\nShapes")

shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()


# Payment System

class Payment:

    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


print("\nPayments")

payments = [CreditCard(), UPI()]

for p in payments:
    p.pay(1000)