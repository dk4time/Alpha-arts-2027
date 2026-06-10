n = int(input())

temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Palindrome" if temp == rev else "Not Palindrome")