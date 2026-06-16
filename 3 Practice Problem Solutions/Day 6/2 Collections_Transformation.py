"""
Topic: Collection Transformations
Author: Dineshkumar
"""

# Matrix Flattening

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    value
    for row in matrix
    for value in row
]

print("Flattened Matrix")
print(flattened)


# Filtering Values

numbers = [10, 15, 20, 25, 30]

filtered = [
    x
    for x in numbers
    if x > 20
]

print("\nFiltered Values")
print(filtered)


# Transformations

names = [
    "john",
    "sam",
    "david"
]

upper_names = [
    name.upper()
    for name in names
]

print("\nTransformed Names")
print(upper_names)