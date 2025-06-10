def f_gold ( p , q ) :
    dp = [ 0 for i in range ( q ) ]
    dp[0] = 1
    for i in range ( p ) :
        for j in range ( 1 , q ) :
            dp [ j ] += dp [ j - 1 ]
    return dp [ q - 1 ]