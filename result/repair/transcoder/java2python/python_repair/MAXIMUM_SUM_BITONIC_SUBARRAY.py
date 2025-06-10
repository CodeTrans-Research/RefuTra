def f_gold ( arr , n ) :
    msis = [ ]
    msds = [ ]
    max_sum = -sys.maxsize
    msis.append ( arr [ 0 ] )
    for i in range ( 1 , n ) :
        if arr [ i ] > arr [ i - 1 ] :
            msis.append ( msis [ i - 1 ] + arr [ i ] )
        else :
            msis.append ( arr [ i ] )
    msds.append ( arr [ n - 1 ] )
    for i in range ( n - 2 , - 1 , - 1 ) :
        if arr [ i ] > arr [ i + 1 ] :
            msds.append ( msds [ i + 1 ] + arr [ i ] )
        else :
            msds.append ( arr [ i ] )
    for i in range ( n ) :
        if max_sum < ( msis [ i ] + msds [ i ] - arr [ i ] ) :
            max_sum = msis [ i ] + msds [ i ] - arr [ i ]
    return max_sum

