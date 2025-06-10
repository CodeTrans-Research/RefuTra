def f_gold ( m , r , c ) :
    mi = sys.maxsize
    mx = - sys.maxsize - 1
    for i in range ( r ) :
        if m [ i ] [ 0 ] < mi :
            mi = m [ i ] [ 0 ]
        if m [ i ] [ c - 1 ] > mx :
            mx = m [ i ] [ c - 1 ]
    desired = ( r * c + 1 ) // 2
    while ( mi < mx ) :
        mid = mi + ( mx - mi ) // 2
        place = [ 0 ]
        for i in range ( r ) :
            j = upper_bound ( m [ i ] , mid )
            place [ 0 ] = place [ 0 ] + j
        if place [ 0 ] < desired :
            mi = mid + 1
        else :
            mx = mid
    print ( "Median is" , mi )
    return mi