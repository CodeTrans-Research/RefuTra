def f_gold ( n , p ) :
    n = n % p
    for x in range ( 2 , p ) :
        if ( x ** 2 ) % p == n :
            return True
    return False
