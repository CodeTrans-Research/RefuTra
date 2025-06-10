def f_gold ( cost , n , W ) :
    val = list ( )
    wt = list ( )
    size = 0
    for i in range ( n ) :
        if ( cost [ i ] != - 1 ) :
            val.append ( cost [ i ] )
            wt.append ( i + 1 )
            size += 1
    n = size
    min_cost = [ [ 0 for i in range ( W + 1 ) ] for j in range ( n + 1 ) ]
    for i in range ( W + 1 ) :
        min_cost [ 0 ] [ i ] = sys.maxsize
    for i in range ( 1 , n + 1 ) :
        min_cost [ i ] [ 0 ] = 0
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , W + 1 ) :
            if ( wt [ i - 1 ] > j ) :
                min_cost [ i ] [ j ] = min_cost [ i - 1 ] [ j ]
            else :
                min_cost [ i ] [ j ] = min ( min_cost [ i - 1 ] [ j ] , min_cost [ i ] [ j - wt [ i - 1 ] ] + val [ i - 1 ] )
    if ( min_cost [ n ] [ W ] == sys.maxsize ) :
        return - 1
    else :
        return min_cost [ n ] [ W ]