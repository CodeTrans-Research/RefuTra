def f_gold ( arr , n ) :
    mls , max = [0 for _ in range(n)], 0
    for i in range ( n ) :
        mls [ i ] = 1
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if abs ( arr [ i ] - arr [ j ] ) <= 1 and mls [ i ] < mls [ j ] + 1 :
                mls [ i ] = mls [ j ] + 1
    for i in range ( n ) :
        if max < mls [ i ] :
            max = mls [ i ]
    return max

