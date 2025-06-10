def f_gold ( n ) :
    l = len ( n )
    count = 0
    if ( l == 1 ) :
        oneDigit = int ( n [ 0 ] )
        if ( oneDigit % 8 == 0 ) :
            return 1
        return 0
    if ( l == 2 ) :
        first = int ( n [ 0 ] ) * 10 + int ( n [ 1 ] )
        second = int ( n [ 1 ] ) * 10 + int ( n [ 0 ] )
        if ( first % 8 == 0 ) :
            count += 1
        if ( second % 8 == 0 ) :
            count += 1
        return count
    threeDigit = 0
    for i in range ( 0 , ( l - 2 ) ) :
        threeDigit = ( int ( n [ i ] ) * 100 + int ( n [ i + 1 ] ) * 10 + int ( n [ i + 2 ] ) )
        if ( threeDigit % 8 == 0 ) :
            count += 1
    threeDigit = ( int ( n [ l - 1 ] ) * 100 + int ( n [ 0 ] ) * 10 + int ( n [ 1 ] ) )
    if ( threeDigit % 8 == 0 ) :
        count += 1
    threeDigit = ( int ( n [ l - 2 ] ) * 100 + int ( n [ l - 1 ] ) * 10 + int ( n [ 0 ] ) )
    if ( threeDigit % 8 == 0 ) :
        count += 1
    return count