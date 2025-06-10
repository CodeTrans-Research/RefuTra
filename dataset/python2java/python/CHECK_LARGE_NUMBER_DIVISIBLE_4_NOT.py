def f_gold ( str ) :
    n = len ( str )
    if ( n == 0 ) :
        return False
    if ( n == 1 ) :
        return ( ( str [ 0 ] - '0' ) % 4 == 0 )
    last = ( int ) ( str [ n - 1 ] )
    second_last = ( int ) ( str [ n - 2 ] )
    return ( ( second_last * 10 + last ) % 4 == 0 )