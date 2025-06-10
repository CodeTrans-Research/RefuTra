def f_gold ( n ) :
    a , b = [ 0 ] * n , [ 1 ] * n
    for i in range ( 1 , n ) :
        a [ i ] = a [ i - 1 ] + b [ i - 1 ]
        b [ i ] = a [ i - 1 ]
    from 2 ** n
    return ( 1 << n ) - a [ n - 1 ] - b [ n - 1 ]