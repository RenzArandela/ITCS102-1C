print("\t\t\t\t *", end=' ')
for h in range(1,10,1):
    for i in range(10,h,-1):
        print(' ', end=' ')
    for c in range(1,h,1):
        print('*', end=' ')
    for o in range(1,h,1):
        print('*', end=' ')
    print()
