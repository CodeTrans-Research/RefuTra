def f_gold ( N ) :
    dp = [ 1 , 2 ]
    i = 2
    do :
        dp [ i ] = dp [ i - 1 ] + dp [ i - 2 ]
    while dp [ i ] <= N :
        i += 1
    return ( i - 2 )
