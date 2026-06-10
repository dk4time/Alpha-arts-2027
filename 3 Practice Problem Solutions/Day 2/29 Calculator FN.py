while True:

    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    print("5.Exit")

    choice = int(input())

    if choice == 5:
        break

    a = int(input())
    b = int(input())

    if choice == 1:
        print(a+b)
    elif choice == 2:
        print(a-b)
    elif choice == 3:
        print(a*b)
    elif choice == 4:
        print(a/b)