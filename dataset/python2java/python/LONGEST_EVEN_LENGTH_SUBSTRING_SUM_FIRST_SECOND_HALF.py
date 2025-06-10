def f_gold ( str ) :
    n = len ( str )
    maxlen = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n , 2 ) :
            length = j - i + 1
            leftsum = 0
            rightsum = 0
            for k in range ( 0 , int ( length / 2 ) ) :
                leftsum += ( int ( str [ i + k ] ) - int ( '0' ) )
                rightsum += ( int ( str [ i + k + int ( length / 2 ) ] ) - int ( '0' ) )
            if ( leftsum == rightsum and maxlen < length ) :
                maxlen = length
    return maxlen