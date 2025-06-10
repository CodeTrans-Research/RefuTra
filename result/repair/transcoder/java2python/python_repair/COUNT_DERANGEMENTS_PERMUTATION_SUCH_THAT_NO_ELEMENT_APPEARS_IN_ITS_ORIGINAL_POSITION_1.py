def f_gold ( n ) :
    der = [0 for _ in range(n+1)]
    for i in range ( 3 , n + 1 ) :
        der [ i ] = ( i - 1 ) * ( der [ i - 1 ] + der [ i - 2 ] )
    return der [ n ]

