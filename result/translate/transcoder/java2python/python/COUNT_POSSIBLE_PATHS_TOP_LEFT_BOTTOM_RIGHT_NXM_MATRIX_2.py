def f_gold ( m , n ) :
    dp = np.zeros ( ( n , m ) )
    dp [ 0 ] = 1
    for i in range ( m ) :
        for j in range ( 1 , n ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ n - 1 ]
