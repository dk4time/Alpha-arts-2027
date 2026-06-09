ch = input("Enter a character: ")

print("ASCII Value:", ord(ch))

ascii = 97

print("ASCII Value:", chr(ascii))

#Find odd or even based on sum of ascii values in the given string
print(ord("a")+ord("b"))

str = input("Enter a string:")
total_ascii=0
for ch in str:
    total_ascii += ord(ch)
print("Total ASCII Value:", total_ascii)

