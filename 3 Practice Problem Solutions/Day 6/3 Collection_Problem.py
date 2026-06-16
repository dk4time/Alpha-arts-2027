"""
Topic: Collection Problems
Author: Dineshkumar
"""

# Frequency Sorting

text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

sorted_freq = sorted(
    freq.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Frequency Sorting")
print(sorted_freq)


# Duplicate Detection

numbers = [10, 20, 30, 20, 40]

seen = set()
duplicate_found = False

for num in numbers:

    if num in seen:
        duplicate_found = True
        break

    seen.add(num)

print("\nDuplicate Detection")
print("Duplicate Found"
      if duplicate_found
      else "No Duplicate")


# Inventory Management

inventory = {
    "Pen": 100,
    "Book": 50,
    "Pencil": 80
}

print("\nInventory")

for item, quantity in inventory.items():
    print(item, quantity)