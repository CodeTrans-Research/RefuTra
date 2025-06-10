def f_gold ( seq ) :
    n = len ( seq )
    if ( n >= 9 ) :
        return "-1"
    result = [ '' ] * ( n + 1 )
    count = 1
    for i in range ( n + 1 ) :
        if ( i == n or seq [ i ] == 'I' ) :
            for j in range ( i - 1 , - 2 , - 1 ) :
                result [ j + 1 ] =  chr ( ord ( '0' ) + count)
                count += 1
                if ( j >= 0 and seq [ j ] == 'I' ) :
                    break
    return ''.join(result)