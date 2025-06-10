def f_gold ( arr , n ) :
    hash = { }
    maximum = 0
    for i in range ( n ) :
        if arr [ i ] < 0 :
            hash [ abs ( arr [ i ] ) ] = ( hash [ abs ( arr [ i ] ) ] if i in hash else 0 ) - 1
        else :
            hash [ abs ( arr [ i ] ) ] = ( hash [ abs ( arr [ i ] ) ] if i in hash else 0 ) + 1
    for i in range ( n ) :
        if hash [ i ] > 0 :
            return arr [ i ]
    return - 1