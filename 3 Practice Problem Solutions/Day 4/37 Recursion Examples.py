#Display numbers
num = int(input("Enter the numbers"))
#
# while n>0:
#     print(n, end=" ")
#     n -= 1

def display(n):
    #Base Condition
    if n == 0:
        return
    #fn body
    print("Function called:1 - ", n)
    #recurison call - iter
    display(n-1)

    print("Function called:2 -", n)

display(num)

def sum_natural(n):

    if n == 0:
        return 1

    return n * sum_natural(n-1)

print(sum_natural(num))

'''
5 0
4 5
3 9
2 12
1 14
0 15
'''







