a = int(input("Enter a: "))
b = int(input("Enter b: "))

#Python Way
a, b = b, a

print("a =", a)
print("b =", b)

#using temp
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)

# arth, bitwise
a = a + b # 10 + 20
b = a - b
b = a - b

print("a =", a)
print("b =", b)


