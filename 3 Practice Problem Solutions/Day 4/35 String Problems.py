"""
Advanced String Programs
"""

# Character Frequency
s = input("Enter String: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("\nCharacter Frequency")
print(freq)


# Anagram Check
s1 = input("\nFirst String: ")
s2 = input("Second String: ")

print("Anagram" if sorted(s1) == sorted(s2)
      else "Not Anagram")


# String Rotation
s = input("\nEnter String: ")
k = int(input("Rotation Count: "))

k %= len(s)

print("Rotated String:", s[k:] + s[:k])


# Compression Basics
s = input("\nEnter String for Compression: ")

result = ""
count = 1

for i in range(len(s)-1):

    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print("Compressed:", result)


# Substring Counting
text = input("\nEnter Main String: ")
sub = input("Enter Substring: ")

print("Occurrences:", text.count(sub))