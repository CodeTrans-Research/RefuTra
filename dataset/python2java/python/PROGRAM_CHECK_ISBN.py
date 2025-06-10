def f_gold ( isbn ) :
    if len ( isbn ) != 10 :
        return False
    _sum = 0
    for i in range ( 9 ) :
        if 0 <= int ( isbn [ i ] ) <= 9 :
            _sum += int ( isbn [ i ] ) * ( 10 - i )
        else :
            return False
    if ( isbn [ 9 ] != 'X' and 0 <= int ( isbn [ 9 ] ) <= 9 ) :
        return False
    _sum += 10 if isbn [ 9 ] == 'X' else int ( isbn [ 9 ] )
    return ( _sum % 11 == 0 )