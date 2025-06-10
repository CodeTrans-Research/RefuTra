def f_gold ( arr , n ) :
    i , j , max = 0 , 0
    msis = [ ]
    for i in range ( n ) :
        msis.append ( arr [ i ] )
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and msis [ i ] < msis [ j ] + arr [ i ] :
                msis [ i ] , msis [ j ] = msis [ j ] , msis [ i ]
    for i in range ( n ) :
        if max < msis [ i ] :
            max = msis [ i ]
    return max
