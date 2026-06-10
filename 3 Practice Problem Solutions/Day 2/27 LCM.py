a = int(input())
b = int(input())

x, y = a, b

while y:
    x, y = y, x % y

gcd = x

print((a * b) // gcd)