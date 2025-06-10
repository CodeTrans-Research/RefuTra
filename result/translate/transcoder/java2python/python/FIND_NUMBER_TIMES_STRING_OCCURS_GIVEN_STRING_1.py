def f_gold ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [ 0 ] * ( m + 1 ) * ( n + 1 )
    for i in range ( 0 , n ) :
        lookup [ 0 ] [ i ] = 0
    for i in range ( 0 , m ) :
        lookup [ i ] [ 0 ] = 1
    for i in range ( 1 , m ) :
        for j in range ( 1 , n ) :
            if a [ i - 1 ] == b [ j - 1 ] :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ]
            else :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ]
    return lookup [ m ] [ n ]
