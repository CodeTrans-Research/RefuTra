def f_gold ( arr , n ) :
    LIS = [ ]
    len = 0
    for i in range ( n ) :
        LIS.append ( 1 )
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if arr [ i ] > arr [ j ] and ( i - j ) <= ( arr [ i ] - arr [ j ] ) :
                LIS [ i ] = max ( LIS [ i ] , LIS [ j ] + 1 )
        len = max ( len , LIS [ i ] )
    return n - len
