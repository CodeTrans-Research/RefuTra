def f_gold ( n ) :
    dp = [ 0 ] * ( n + 1 )
    dp [ 0 ] = 1
    for i in range ( 2 , n + 1 ) :
        dp [ i ] = max ( dp [ i // 2 ] + dp [ i // 3 ] + dp [ i // 4 ] , i )
    return dp [ n ]

