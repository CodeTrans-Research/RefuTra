def f_gold ( arr , N ) :
    arr = np.array ( arr )
    if N < 3 :
        return False
    arr.sort ( )
    for i in range ( N - 2 ) :
        if arr [ i ] + arr [ i + 1 ] > arr [ i + 2 ] :
            return True
    return False