"""
Topic: Dictionaries
Author: Dineshkumar
"""

# Creating Dictionaries

student = {
    "id": 101,
    "name": "John",
    "marks": 95
}

print(student)


# Accessing Values

print(student["name"])


# get(key, default=None)
# dict | Params: key (Required), default (Optional) | Returns: Any | O(1)

print(student.get("marks"))
print(student.get("city", "Not Found"))


# Adding / Updating Values

student["city"] = "Chennai"
student["marks"] = 98

print(student)


# keys()
# dict | Params: None | Returns: dict_keys | O(1)

print(student.keys())


# values()
# dict | Params: None | Returns: dict_values | O(1)

print(student.values())


# items()
# dict | Params: None | Returns: dict_items | O(1)

print(student.items())


# pop(key)
# dict | Params: key (Required) | Returns: value | O(1)

removed = student.pop("city")

print(removed)
print(student)


# popitem()
# dict | Params: None | Returns: tuple | O(1)

print(student.popitem())


# update(other)
# dict | Params: dict (Required) | Returns: None | O(n)

student.update({
    "department": "MCA",
    "year": 2
})

print(student)


# Membership

print("name" in student)
print("salary" in student)


# Traversing Dictionary

for key in student:
    print(key, student[key])


# Traversing items()

for key, value in student.items():
    print(key, value)


# len()
# Built-in Function | Params: iterable | Returns: int | O(1)

print(len(student))


# ------------------------------------------
# zip()
# ------------------------------------------

names = ["John", "Sam", "David"]
marks = [95, 88, 91]

student_marks = dict(zip(names, marks))

print(student_marks)


# ------------------------------------------
# max()
# ------------------------------------------

scores = {
    "John": 95,
    "Sam": 88,
    "David": 91
}

print(max(scores))                # Max Key
print(max(scores.values()))       # Max Value
print(max(scores, key=scores.get))  # Key with Max Value


# ------------------------------------------
# min()
# ------------------------------------------

print(min(scores))                # Min Key
print(min(scores.values()))       # Min Value
print(min(scores, key=scores.get))  # Key with Min Value


# ------------------------------------------
# sum()
# ------------------------------------------

print(sum(scores.values()))


# ------------------------------------------
# sorted()
# ------------------------------------------

# Sort by Keys

print(sorted(scores))

# Sort by Values (Ascending)

print(sorted(scores.items(), key=lambda x: x[1]))

# Sort by Values (Descending)

print(sorted(scores.items(),
             key=lambda x: x[1],
             reverse=True))


# ------------------------------------------
# Dictionary Comprehension
# ------------------------------------------

square = {x: x*x for x in range(1, 6)}

print(square)


# ------------------------------------------
# clear()
# ------------------------------------------

temp = {"a": 1, "b": 2}

temp.clear()

print(temp)


# ------------------------------------------
# copy()
# ------------------------------------------

original = {
    "name": "John",
    "age": 20
}

duplicate = original.copy()

print(duplicate)