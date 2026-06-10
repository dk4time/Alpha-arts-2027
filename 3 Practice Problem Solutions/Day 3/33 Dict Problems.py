# Student Records
students = {
    101: "John",
    102: "David",
    103: "Sam"
}

print("Student Records")
for roll, name in students.items():
    print(roll, name)

# Phone Book
phonebook = {
    "John": "9876543210",
    "Sam": "9999999999",
    "David": "8888888888"
}

name = input("\nEnter Name to Search: ")
print("Phone Number:", phonebook.get(name, "Not Found"))

# Inventory Management
inventory = {
    "Pen": 100,
    "Book": 50,
    "Pencil": 80
}

print("\nInventory")
for item, qty in inventory.items():
    print(item, qty)

# Frequency Count
nums = [10, 20, 10, 30, 20, 10]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print("\nFrequency Count")
print(freq)

# Duplicate Detection
nums = [10, 20, 30, 20, 40]

seen = set()
duplicate_found = False

for num in nums:
    if num in seen:
        duplicate_found = True
        break
    seen.add(num)

print("\nDuplicate Found" if duplicate_found else "\nNo Duplicate")

# Word Frequency
text = "python is easy python is powerful"

words = text.split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord Frequency")
print(word_freq)