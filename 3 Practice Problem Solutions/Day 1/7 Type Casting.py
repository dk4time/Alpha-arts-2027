num = 10.75

converted = int(num)

print("Before:", num)
print("After:", converted)

# string casting
num_str = str(num)  
# display number of digits
print("Number of digits in", num_str, "is", len(num_str.replace('.', '')))