def f_gold ( A , K ) :
    n = len ( A )
    pre_sum = np.zeros ( ( n + 1 , ) )
    pre_sum [ 0 ] = 0
    for i in range ( n ) :
        pre_sum [ i + 1 ] = pre_sum [ i ] + A [ i ]
    dp = np.zeros ( ( n , ) )
    sum = 0
    for i in range ( n ) :
        dp [ i ] = ( pre_sum [ n ] - pre_sum [ i ] ) / ( n - i )
    for k in range ( K - 1 ) :
        for i in range ( n ) :
            for j in range ( i + 1 , n ) :
                dp [ i ] = max ( dp [ i ] , ( pre_sum [ j ] - pre_sum [ i ] ) / ( j - i ) + dp [ j ] )
    return dp
