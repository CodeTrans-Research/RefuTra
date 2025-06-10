def f_gold ( arr , N , K ) :
    arr.sort ( )
    dp = [ 0 ] * N
    i=1 
    while i<N :
        dp [ i ] = dp [ i - 1 ]
        if arr [ i ] - arr [ i - 1 ] < K :
            if i >= 2 :
                dp [ i ] = max ( dp [ i ] , dp [ i - 2 ] + arr [ i ] + arr [ i - 1 ] )
            else :
                dp [ i ] = max ( dp [ i ] , arr [ i ] + arr [ i - 1 ] )
        i += 1
    return dp [ N - 1 ]

