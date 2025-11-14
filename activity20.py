for i in range (1,11,1):
    for x in range(10,i,-1):
        print(' ', end = '')
    for y in range(1,i,1):
        print('*', end = '')
    for z in range (1,i,1):
        print('*', end = '')
    print()

for b in range (1,11,1):
    for l in range(b,1,-1):
        print(' ', end = '')
    for c in range(10,b,-1):
        print('*', end = '')
    for k in range (10,b,-1):
        print('*', end = '')
    print()