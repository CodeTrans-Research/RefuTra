def f_gold ( a , b ) :
    if a == 0 :
        return b
    if b == 0 :
        return a
    k = 0
    for ( ( a | b ) & 1 ) == 0 :
        a >>= 1
        b >>= 1
    while ( a & 1 ) == 0 :
        a >>= 1
    do :
        while ( b & 1 ) == 0 :
            b >>= 1
        if a > b :
            temp = a
            a , b = b , temp
        b = ( b - a )
    while b != 0 :
        return a << k