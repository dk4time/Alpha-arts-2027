"""
Searching & Sorting Programs
"""

nums = list(map(int, input("Enter Numbers: ").split()))

target = int(input("Search Element: "))

# Search Element
print("\nSearch Result")
print("Found" if target in nums else "Not Found")

# Occurrence Count
print("\nOccurrence Count")
print(nums.count(target))

# First Occurrence
print("\nFirst Occurrence")
print(nums.index(target) if target in nums else -1)


# Kth Largest
k = int(input("\nEnter K: "))

print("Kth Largest:",
      sorted(nums, reverse=True)[k-1])


# Sorting Records
students = [
    ("John", 85),
    ("Sam", 92),
    ("David", 78),
    ("Alex", 88)
]

print("\nSorted by Marks")

students.sort(key=lambda x: x[1])

for student in students:
    print(student)

print("\nSorted Descending")

students.sort(
    key=lambda x: x[1],
    reverse=True
)

for student in students:
    print(student)