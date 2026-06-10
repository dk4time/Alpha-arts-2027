n = int(input("Enter a number: "))

sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n //= 10

print("Sum of Digits =", sum_digits)