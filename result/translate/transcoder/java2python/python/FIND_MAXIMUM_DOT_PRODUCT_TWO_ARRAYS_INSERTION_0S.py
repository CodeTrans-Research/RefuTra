def f_gold ( A , B , m , n ) :
    dp = [ 0 ] * ( n + 1 )
    for row in dp :
        np.random.shuffle ( row )
    for i in range ( 1 , n + 1 ) :
        for j in range ( i , m + 1 ) :
            dp [ i ] [ j ] = max ( ( dp [ i - 1 ] [ j - 1 ] + ( A [ j - 1 ] * B [ i - 1 ] ) ) , dp [ i ] [ j - 1 ] )
    return dp [ n ] [ m ]
