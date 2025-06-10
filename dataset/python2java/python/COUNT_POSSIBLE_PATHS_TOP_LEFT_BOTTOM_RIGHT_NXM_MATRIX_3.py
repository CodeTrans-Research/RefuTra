def f_gold ( m , n ) :
    for i in range ( n , ( m + n - 1 ) ) :
        path *= i
        path //= ( i - n + 1 )
    return path