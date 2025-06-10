def f_gold ( degree , n ) :
    deg_sum = 0
    for i in range ( n ) :
        deg_sum += degree [ i ]
    return ( 2 ** ( n - 1 ) == deg_sum )
