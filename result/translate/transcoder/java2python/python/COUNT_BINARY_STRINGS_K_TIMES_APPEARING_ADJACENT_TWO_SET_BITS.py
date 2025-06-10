def f_gold ( n , k ) :
    dp = [ [ 1 , 1 ] , [ 1 , 1 ] ]
    dp [ 1 ] [ 0 ] [ 0 ] = 1
    dp [ 1 ] [ 0 ] [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        for j in range ( 0 , i + 1 , k + 1 ) :
            dp [ i ] [ j ] [ 0 ] = dp [ i - 1 ] [ j ] [ 0 ] + dp [ i - 1 ] [ j ] [ 1 ]
            dp [ i ] [ j ] [ 1 ] = dp [ i - 1 ] [ j ] [ 0 ]
            if j - 1 >= 0 :
                dp [ i ] [ j ] [ 1 ] += dp [ i - 1 ] [ j - 1 ] [ 1 ]
    return dp [ n ] [ k ] [ 0 ] + dp [ n ] [ k ] [ 1 ]
