def f_gold ( a , b ) :
    m = len ( a )
    n = len ( b )
    lookup = [[0 for _ in range(n+1)] for _ in range(m+1)]
    i=0 
    while i<n+1 :
        lookup [ 0 ] [ i ] = 0
        i += 1
    i=0 
    while i<m+1 :
        lookup [ i ] [ 0 ] = 1
        i += 1
    i=1 
    while i<m+1 :
        j=1 
        while j<n+1 :
            if a [ i - 1 ] == b [ j - 1 ] :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j - 1 ] + lookup [ i - 1 ] [ j ]
            else :
                lookup [ i ] [ j ] = lookup [ i - 1 ] [ j ]
            j += 1
        i += 1
    return lookup [ m ] [ n ]

