def f_gold ( arr , n ) :
    d = { }
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            d [ arr [ i ] + arr [ j ] ] = Indexes ( i , j )
    d = -sys.maxsize
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            abs_diff = abs ( arr [ i ] - arr [ j ] )
            if d.has_key ( abs_diff ) :
                indexes = d [ abs_diff ]
                if indexes [ 'i' ] != i and indexes [ 'i' ] != j and indexes [ 'j' ] != i and indexes [ 'j' ] != j :
                    d = max ( d , max ( arr [ i ] , arr [ j ] ) )
    return int(d) 
