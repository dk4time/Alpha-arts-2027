n = int(input())

temp = n
s = 0

while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    s += fact
    temp //= 10

print("Strong" if s == n else "Not Strong")

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

n = int(input())

print("Prime" if is_prime(n) else "Not Prime")