def f_gold ( p , i , j ) :
    if i == j :
        return 0
    _min = sys.maxsize
    for k in range ( i , j ) :
        count = ( f_gold ( p , i , k ) + f_gold ( p , k + 1 , j ) + p [ i - 1 ] * p [ k ] * p [ j ] )
        if count < _min :
            _min = count
    return _min