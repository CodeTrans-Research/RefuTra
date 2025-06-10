def f_gold ( num ) :
    n = len ( num )
    if ( n == 0 and num [ 0 ] == '\n' ) :
        return 1
    if ( n % 3 == 1 ) :
        num = str ( num ) + "00"
        n += 2
    elif ( n % 3 == 2 ) :
        num = str ( num ) + "0"
        n += 1
    GSum = 0
    p = 1
    for i in range ( n - 1 , - 1 , - 1 ) :
        group = 0
        group += ord ( num [ i ] ) - ord ( '0' )
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 10
        i -= 1
        group += ( ord ( num [ i ] ) - ord ( '0' ) ) * 100
        GSum = GSum + group * p
        p *= ( - 1 )
    return ( GSum % 7 == 0 )