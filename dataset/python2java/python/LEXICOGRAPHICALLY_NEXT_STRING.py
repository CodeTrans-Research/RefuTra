def f_gold ( s ) :
    if ( s == " " ) :
        return "a"
    i = len ( s ) - 1
    while ( s [ i ] == 'z' and i >= 0 ) :
        i -= 1
    if ( i == - 1 ) :
        s = s + 'a'
    else :
        s = s [ 0 : i ] + chr ( ord ( s [ i ] ) + 1 ) + s [ i + 1 : ]
    return s