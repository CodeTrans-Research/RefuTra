def f_gold ( n , i ) :
    if ( n <= 2 ) :
        return True if ( n == 2 ) else False
    if ( n % i == 0 ) :
        return False
    if ( i * i > n ) :
        return true
    return f_gold ( n , i + 1 )