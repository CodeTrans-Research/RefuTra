def f_gold ( arr , n , k ) :
    if k > n :
        return - 1
    csum = [ arr [ i ] for i in range ( n ) ]
    for i in range ( 1 , n ) :
        csum [ i ] = csum [ i - 1 ] + arr [ i ]
    max_sum , max_end = csum [ k - 1 ] , k - 1
    for i in range ( k , n ) :
        curr_sum = csum [ i ] - csum [ i - k ]
        if curr_sum > max_sum :
            max_sum = curr_sum
            max_end = i
    return max_end - k + 1
