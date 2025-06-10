def f_gold ( arr , n ) :
    sum = [ ]
    if n >= 1 :
        sum.append ( arr [ 0 ] )
    if n >= 2 :
        sum.append ( arr [ 0 ] + arr [ 1 ] )
    if n > 2 :
        sum.append ( max ( sum [ 1 : ] , max ( arr [ 1 : ] + arr [ 2 : ] , arr [ 0 ] + arr [ 2 ] ) ) )
    for i in range ( 3 , n ) :
        sum.append ( max ( max ( sum [ - 1 ] , sum [ - 2 ] + arr [ i ] ) , arr [ i ] + arr [ i - 1 ] + sum [ - 3 ] ) )
    return sum [ - 1 ]
