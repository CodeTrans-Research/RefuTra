def f_gold ( str ) :
    n = len ( str )
    dp = [ 0 ] * n + [ 0 ] * n + [ 0 ] * n
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            if str [ i - 1 ] == str [ j - 1 ] and i != j :
                dp [ i ] [ j ] = 1 + dp [ i - 1 ] [ j - 1 ]
            else :
                dp [ i ] [ j ] = max ( dp [ i ] [ j - 1 ] , dp [ i - 1 ] [ j ] )
    return dp [ n ] [ n ]
