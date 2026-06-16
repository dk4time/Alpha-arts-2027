"""
Topic: Errors & Debugging
Author: Dineshkumar
"""

# =====================================
# Syntax Error
# =====================================

print("Syntax Error Example")

# Uncomment to see syntax error

# if True
#     print("Hello")


# =====================================
# Logical Error
# =====================================

print("\nLogical Error Example")

a = 10
b = 20

# Wrong Logic

if a > b:
    print("B is Greater")
else:
    print("A is Greater")

print("Expected Output: B is Greater")


# =====================================
# Runtime Error
# =====================================

print("\nRuntime Error Example")

try:

    num = 10
    den = 0

    print(num / den)

except ZeroDivisionError:
    print("Division By Zero")


# =====================================
# Value Error
# =====================================

print("\nValue Error Example")

try:

    age = int("abc")

except ValueError:
    print("Invalid Integer")


# =====================================
# Index Error
# =====================================

print("\nIndex Error Example")

try:

    numbers = [10, 20, 30]

    print(numbers[10])

except IndexError:
    print("Index Out Of Range")