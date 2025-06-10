def f_gold ( arr , n ) :
    temp = [ ]
    j = 0
    for i in range ( n ) :
        if arr [ i ] >= 0 :
            temp.append ( arr [ i ] )
    if j == n or j == 0 :
        return
    for i in range ( n ) :
        if arr [ i ] < 0 :
            temp.append ( arr [ i ] )
    for i in range ( n ) :
        arr [ i ] = temp [ i ]