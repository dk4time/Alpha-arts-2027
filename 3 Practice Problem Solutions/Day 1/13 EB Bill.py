units = int(input("Enter units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 200 * 2.5 + (units - 300) * 4

print("Bill Amount =", bill)