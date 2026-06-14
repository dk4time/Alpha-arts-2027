"""
Topic: Exception Handling
Author: Digital Flash Notes
"""

# ==================================================
# Example 1: Zero Division
# ==================================================

print("=== Zero Division Example ===")

try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


# ==================================================
# Example 2: Value Error
# ==================================================

print("\n=== Value Error Example ===")

try:
    age = int("abc")

except ValueError:
    print("Invalid Number Format")


# ==================================================
# Example 3: Index Error
# ==================================================

print("\n=== Index Error Example ===")

try:
    nums = [10, 20, 30]

    print(nums[5])

except IndexError:
    print("Index Out of Range")


# ==================================================
# Example 4: Key Error
# ==================================================

print("\n=== Key Error Example ===")

try:
    student = {
        "name": "John"
    }

    print(student["marks"])

except KeyError:
    print("Key Not Found")


# ==================================================
# Example 5: Multiple Exceptions
# ==================================================

print("\n=== Multiple Exception Example ===")

try:

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print(a / b)

except ValueError:
    print("Enter Numbers Only")

except ZeroDivisionError:
    print("Cannot Divide By Zero")


# ==================================================
# Example 6: Finally Block
# ==================================================

print("\n=== Finally Example ===")

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Execution Completed")


# ==================================================
# Example 7: ATM Simulation
# ==================================================

class ATM:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        try:

            if amount > self.balance:
                raise Exception("Insufficient Balance")

            self.balance -= amount

            print("Withdrawal Successful")

        except Exception as e:
            print(e)

        finally:
            print("Available Balance:", self.balance)


print("\n=== ATM Example ===")

atm = ATM(10000)

atm.withdraw(3000)
atm.withdraw(15000)


# ==================================================
# Example 8: Student Marks System
# ==================================================

print("\n=== Student Marks Example ===")

try:

    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    print("Valid Marks")

except ValueError as e:
    print(e)


# ==================================================
# Example 9: Custom Exception
# ==================================================

class InvalidAgeError(Exception):
    pass


print("\n=== Custom Exception Example ===")

try:

    age = int(input("Enter Age: "))

    if age < 18:
        raise InvalidAgeError(
            "Age must be 18 or above"
        )

    print("Eligible")

except InvalidAgeError as e:
    print(e)


# ==================================================
# Example 10: File Handling Exception
# ==================================================

print("\n=== File Exception Example ===")

try:

    file = open("sample.txt")

    print(file.read())

except FileNotFoundError:
    print("File Not Found")