def f_gold ( arr , n ) :
    min_prefix_sum = 0
    res = -sys.maxsize
    prefix_sum = [0 for _ in range(n)]
    for i in range ( 1 , n ) :
        prefix_sum [ i ] = prefix_sum [ i - 1 ] + arr [ i ]
    for i in range ( n ) :
        res = max ( res , prefix_sum [ i ] - min_prefix_sum )
        min_prefix_sum = min ( min_prefix_sum , prefix_sum [ i ] )
    return res

