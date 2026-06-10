n = int(input())

digits = len(str(n))
temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

print("Armstrong" if total == n else "Not Armstrong")