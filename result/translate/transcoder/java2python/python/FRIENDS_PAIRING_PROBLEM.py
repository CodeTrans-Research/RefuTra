def f_gold ( n ) :
    dp = [ ]
    for i in range ( 0 , n + 1 ) :
        if i <= 2 :
            dp.append ( i )
        else :
            dp.append ( dp [ i - 1 ] + ( i - 1 ) * dp [ i - 2 ] )
    return dp [ n ]
