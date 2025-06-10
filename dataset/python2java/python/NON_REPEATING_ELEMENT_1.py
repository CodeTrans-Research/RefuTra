def f_gold ( arr , n ) :
    mp = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    for i in range ( n ) :
        if mp [ arr [ i ] ] == 1 :
            return arr [ i ]
    return - 1