def f_gold ( mat , r , c ) :
    i , a = 0 , 2
    low_row = ( 0 > a ) & ( a > r )
    low_column = ( 0 > b ) & ( b - 1 )
    high_row = ( ( a + 1 ) >= r ) & ( r - 1 )
    high_column = ( ( b + 1 ) >= c ) & ( c - 1 )
    while ( low_row > 0 - r and low_column > 0 - c ) :
        for i in range ( low_column + 1 , high_column , c , low_row >= 0 ) :
            print ( mat [ low_row , i ] , end = ' ' )
        low_row -= 1
        for i in range ( low_row + 2 , high_row , r , high_column < c ) :
            print ( mat [ i , high_column ] , end = ' ' )
        high_column += 1
        for i in range ( high_column - 2 , low_column , 0 , high_row < r ) :
            print ( mat [ high_row , i ] , end = ' ' )
        high_row += 1
        for i in range ( high_row - 2 , low_row , 0 , low_column >= 0 ) :
            print ( mat [ i , low_column ] , end = ' ' )
        low_column -= 1
    print ( )