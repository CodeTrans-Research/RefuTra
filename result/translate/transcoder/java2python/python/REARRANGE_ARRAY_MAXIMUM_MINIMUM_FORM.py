def f_gold ( arr , n ) :
    temp = [ ]
    small , large = 0 , n - 1
    flag = True
    for i in range ( n ) :
        if flag :
            temp.append ( arr [ large ] )
        else :
            temp.append ( arr [ small ] )
        flag = not flag
    for k in range ( n ) :
        arr [ k ] = temp [ k ]
    return arr