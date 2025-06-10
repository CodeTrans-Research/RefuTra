def f_gold ( str ) :
    sum = 0
    n = len ( str )
    for i in range ( 0 , n ) :
        sum += ord ( str [ i ] ) - ord ( '0' )
    return ( sum == n - 1 or sum == 1 )