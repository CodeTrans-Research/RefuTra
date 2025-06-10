def f_gold ( n ) :
    ar = [ 0 ] * 10
    while ( n > 0 ) :
        digit = math.floor ( n % 10 )
        if ( ar [ digit ] ) :
            return False
        ar [ digit ] = 1
        n = int ( n / 10 )
    return True