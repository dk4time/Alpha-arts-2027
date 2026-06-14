"""
Real World OOP Applications
"""

# Counter Class

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def display(self):
        print(self.count)


counter = Counter()

counter.increment()
counter.increment()

print("Counter Value")
counter.display()


# Company Employee Tracker

class Company:

    def __init__(self):
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)

    def display(self):
        print(self.employees)


company = Company()

company.add_employee("John")
company.add_employee("David")

print("\nEmployees")
company.display()


# ATM Simulation

class ATM:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(self.balance)


atm = ATM(10000)

atm.deposit(2000)
atm.withdraw(3000)

print("\nBalance")
atm.show_balance()


# Secure User Profile

class User:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def verify(self, pwd):
        return self.__password == pwd


user = User("admin", "1234")

print("\nLogin Status")
print(user.verify("1234"))