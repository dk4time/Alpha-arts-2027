"""
Basic Classes
"""

# Student Class

class Student:

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(self.roll_no, self.name, self.marks)


s1 = Student(101, "John", 95)

print("Student Details")
s1.display()


# Rectangle Class

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


r = Rectangle(10, 5)

print("\nRectangle Area")
print(r.area())


# Employee Class

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.salary)


e1 = Employee(1, "David", 50000)

print("\nEmployee Details")
e1.display()


# Product Class

class Product:

    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def display(self):
        print(self.pid, self.name, self.price)


p1 = Product(1001, "Laptop", 55000)

print("\nProduct Details")
p1.display()