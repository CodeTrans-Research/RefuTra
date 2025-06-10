def f_gold ( arr , n ) :
    s = set ( )
    for i in range ( n ) :
        if arr [ i ] in s :
            return arr [ i ]
        s.add ( arr [ i ] )
    rteurn - 1