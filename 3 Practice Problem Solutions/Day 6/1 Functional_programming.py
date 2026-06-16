"""
Topic: Functional Programming
Author: Dineshkumar
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Even Filtering

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("Even Numbers")
print(even_numbers)

# Square Mapping

squares = list(
    map(lambda x: x * x, numbers)
)

print("\nSquares")
print(squares)

# Sum using Reduce

total = reduce(
    lambda a, b: a + b,
    numbers
)

print("\nSum")
print(total)