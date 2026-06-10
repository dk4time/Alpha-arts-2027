# Input String
s = input("Enter a String: ")

# Reverse String
print("\nReverse String:")
print(s[::-1])

# Palindrome String
print("\nPalindrome Check:")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count Vowels
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("\nVowel Count:", count)

# Reverse Words
print("\nReverse Words:")
words = s.split()
print(" ".join(words[::-1]))

# Toggle Case
print("\nToggle Case:")
print(s.swapcase())

# Remove Spaces
print("\nRemove Spaces:")
print(s.replace(" ", ""))