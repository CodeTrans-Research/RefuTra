def f_gold ( arr , n ) :
    diff = sys.maxsize
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            if abs ( ( arr [ i ] - arr [ j ] ) ) < diff :
                diff = abs ( ( arr [ i ] - arr [ j ] ) )
    return diff
