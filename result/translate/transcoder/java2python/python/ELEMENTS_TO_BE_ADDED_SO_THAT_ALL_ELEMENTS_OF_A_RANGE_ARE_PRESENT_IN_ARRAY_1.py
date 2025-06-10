def f_gold ( arr , n ) :
    s = set ( )
    count , maxm , minm = 0 , int ( min ( arr ) ) , int ( max ( arr ) )
    for i in range ( n ) :
        s.add ( arr [ i ] )
        if arr [ i ] < minm :
            minm = arr [ i ]
        if arr [ i ] > maxm :
            maxm = arr [ i ]
    for i in range ( minm , maxm + 1 ) :
        if not s.add ( i ) :
            count += 1
    return count
