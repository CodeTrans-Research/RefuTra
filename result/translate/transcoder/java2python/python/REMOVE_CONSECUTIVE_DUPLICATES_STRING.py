def f_gold ( S ) :
    n = len ( S )
    if n < 2 :
        return
    j = 0
    for i in range ( 1 , n ) :
        if S [ j ] != S [ i ] :
            j += 1
            S [ j ] = S [ i ]
    print ( sum ( S [ i : i + 1 ] for i in range ( j + 1 , n ) ) )