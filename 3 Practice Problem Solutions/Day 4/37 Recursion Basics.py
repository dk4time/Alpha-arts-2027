"""
Recursion Programs
"""

# Factorial
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


# Sum of Digits
def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n//10)


# Palindrome
def palindrome(s):

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])


# Power
def power(a, b):

    if b == 0:
        return 1

    return a * power(a, b-1)


n = int(input("Enter Number: "))

print("\nFactorial")
print(factorial(n))

print("\nFibonacci Series")

for i in range(n):
    print(fibonacci(i), end=" ")

print()

print("\nDigit Sum")
print(digit_sum(n))

s = input("\nEnter String: ")

print("\nPalindrome Check")
print("Palindrome"
      if palindrome(s)
      else "Not Palindrome")

a = int(input("\nBase: "))
b = int(input("Exponent: "))

print("\nPower")
print(power(a, b))