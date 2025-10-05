for l in range(1, 6 + 1):
    for i in range(6, l, -1):
        print(" ", end=" ")
    for c in range(l, 0, -1):
        print(c, end=" ")
    for o in range(2, l + 1):
        print(o, end=" ")

    print()
    
