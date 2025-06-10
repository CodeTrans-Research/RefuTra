def f_gold ( arr , n ) :
    evenArr = [ ]
    oddArr = [ ]
    for i in range ( n ) :
        if i % 2 != 1 :
            evenArr.append ( arr [ i ] )
        else :
            oddArr.append ( arr [ i ] )
    evenArr.sort ( )
    oddArr.sort ( )
    i = 0
    for j in evenArr :
        arr [ i ] = evenArr [ j ]
    for j in oddArr :
        arr [ i ] = oddArr [ j ]
    return arr