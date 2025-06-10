def f_gold ( arr , n ) :
    arr.sort ( key = lambda x : x [ 1 ] )
    dimension = [ 0 , 0 ]
    for i , j in enumerate ( arr ) :
        if arr [ i ] == arr [ i + 1 ] :
            dimension [ j ] = arr [ i ++ ]
    return ( dimension [ 0 ] * dimension [ 1 ] )
