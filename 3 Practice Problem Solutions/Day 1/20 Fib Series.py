n = int(input("Enter number of terms: "))

a = 0
b = 1

#a b c
 # a  b
#0 1 1
for i in range(n-1):
    # print(a, end=" ")
    c = a + b
    a, b = b , c
print(a)

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

n = int(input())
fibonacci(n)

