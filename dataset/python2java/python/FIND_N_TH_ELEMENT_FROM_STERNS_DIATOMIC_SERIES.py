def f_gold ( n ) :
    DP = [ 0 ] * ( n + 1 )
    DP [ 0 ] = 0
    DP [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        if ( int ( i % 2 ) == 0 ) :
            DP [ i ] = DP [ int ( i / 2 ) ]
        else :
            DP [ i ] = ( DP [ int ( ( i - 1 ) / 2 ) ] + DP [ int ( ( i + 1 ) / 2 ) ] )
    return DP [ n ]