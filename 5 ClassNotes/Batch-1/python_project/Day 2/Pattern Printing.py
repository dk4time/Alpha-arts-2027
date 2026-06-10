row = int(input("row"))
col = int(input("col"))

for i in range(1,row+1):

    for j in range(1, col+1):

        print("*", end="")

        if j!=col:
            print("-", end="")
    print()

print("Right angle triange")
for i in range(1,row+1):

    for j in range(1, i+1):

        print("*", end="")

        if j!=i:
            print("-", end="")
    print()

print("left angle triange")
for i in range(1,row+1):

    #space
    for sp in range(1, row-i+1):
        print("  ", end="")


    for j in range(1, i+1):

        print("*", end="")

        if j!=i:
            print("-", end="")
    print()

print("pramid")
for i in range(1,row+1):

    #space
    for sp in range(1, row-i+1):
        print("  ", end="")


    for j in range(1, 2*i-1+1):

        print("*", end="")

        if j!=2*i-1:
            print("-", end="")
    print()