#list tuple dict set
# creation
list1 = []

list1  = [0] * 10

list1 = [1, 2, 3, 4, 5]

#traversal - access
print(list1[3])
print(list1[-2])

for i in range(len(list1)):
    print(list1[i], end=" ")
print()

for ele in list1:
    print(ele, end=" ")

#modify - insert, update, del
list1 = []
list1.append(1)
list1.append(2)
list1.append(3)

list1.insert(0, 10)

list2 = [10, 20, 30]
list1.extend(list2)

print(list1)

list1[0] = 100
print(list1)

popped = list1.pop(0)
print(popped, list1)

list1.remove(10)
print(list1)

list1.clear()

ind = list1.index(10)
print(ind, list1)

list1.sort(reverse=True)

matrix = [[], [], "",(), {}]

tup1 = (1, 2, 3)

tup1.count(3)



