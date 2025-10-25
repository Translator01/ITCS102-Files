for i in range( 1, 7, 1 ):
    for x in range( 6, i, -1 ):
        print(" ", end=" ")
    for y in range( i, 0, -1 ):
        print( y, end=" ")
    for z in range( 2, i + 1, 1 ):
        print( z, end=" " )
    print()