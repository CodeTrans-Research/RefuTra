def f_gold ( str , n ) :
    l = len ( str )
    dp = [ [ 0 for x in range ( n ) ] for y in range ( l ) ]
    dp [ 0 ] [ ( ord ( str [ 0 ] ) - ord ( '0' ) ) % n ] += 1
    for i in range ( 1 , l ) :
        dp [ i ] [ ( ord ( str [ i ] ) - ord ( '0' ) ) % n ] += 1
        for j in range ( n ) :
            dp [ i ] [ j ] += dp [ i - 1 ] [ j ]
            dp [ i ] [ ( j * 10 + ( ord ( str [ i ] ) - ord ( '0' ) ) ) % n ] += dp [ i - 1 ] [ j ]
    return dp [ l - 1 ] [ 0 ]