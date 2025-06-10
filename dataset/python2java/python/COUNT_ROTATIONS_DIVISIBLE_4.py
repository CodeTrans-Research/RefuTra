def f_gold ( n ) :
    l = len ( n )
    if ( l == 1 ) :
        oneDigit = ( int ) ( n [ 0 ] )
        if ( oneDigit % 4 == 0 ) :
            return 1
        return 0
    count = 0
    for i in range ( 0 , l - 1 ) :
        twoDigit = ( int ) ( n [ i ] ) * 10 + ( int ) ( n [ i + 1 ] )
        if ( twoDigit % 4 == 0 ) :
            count = count + 1
    twoDigit = ( int ) ( n [ l - 1 ] ) * 10 + ( int ) ( n [ 0 ] )
    if ( twoDigit % 4 == 0 ) :
        count = count + 1
    return count