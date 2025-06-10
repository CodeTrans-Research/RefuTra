def f_gold ( n ) :
    arr = [ [ abs ( i - j ) for j in range ( n ) ] for i in range ( n ) ]
    sum = 0
    for i in range ( n ) :
        for j in range ( n ) :
            sum += arr [ i ] [ j ]
    return sum
