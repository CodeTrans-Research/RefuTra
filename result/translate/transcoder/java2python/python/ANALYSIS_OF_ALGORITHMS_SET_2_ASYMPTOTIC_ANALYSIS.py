def f_gold ( arr , n , x ) :
    i = 0
    for i in range ( n ) :
        if arr [ i ] == x :
            return i
    return - 1
