"""
Topic: OOP Problem Solving
Author: Dineshkumar
"""

# ==================================================
# Library Management System
# ==================================================

class Book:

    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def issue(self):

        if self.available:
            self.available = False
            print(self.title, "Issued")
        else:
            print(self.title, "Already Issued")

    def return_book(self):
        self.available = True
        print(self.title, "Returned")


print("=== Library Management ===")

book1 = Book(101, "Python Programming")

book1.issue()
book1.issue()
book1.return_book()


# ==================================================
# Banking System
# ==================================================

class BankAccount:

    def __init__(self, account_no, holder, balance):

        self.account_no = account_no
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):

        self.__balance += amount

        print("Deposited:", amount)

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print("Withdrawn:", amount)

        else:
            print("Insufficient Balance")

    def show_balance(self):

        print("Balance:", self.__balance)


print("\n=== Banking System ===")

acc = BankAccount(
    1001,
    "John",
    10000
)

acc.deposit(2000)
acc.withdraw(3000)
acc.show_balance()


# ==================================================
# Employee Management System
# ==================================================

class Employee:

    def __init__(self, emp_id, name):

        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(
        self,
        emp_id,
        name,
        monthly_salary
    ):

        super().__init__(emp_id, name)

        self.monthly_salary = monthly_salary

    def calculate_salary(self):

        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(
        self,
        emp_id,
        name,
        hours,
        rate
    ):

        super().__init__(emp_id, name)

        self.hours = hours
        self.rate = rate

    def calculate_salary(self):

        return self.hours * self.rate


print("\n=== Employee Management ===")

employees = [

    FullTimeEmployee(
        1,
        "David",
        50000
    ),

    PartTimeEmployee(
        2,
        "Sam",
        40,
        500
    )
]

for emp in employees:

    print(
        emp.name,
        "Salary:",
        emp.calculate_salary()
    )