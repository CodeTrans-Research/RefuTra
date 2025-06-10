def f_gold ( arr , n ) :
    um = defaultdict ( lambda : 0 )
    longLen = 0
    for i in range ( n ) :
        len1 = 0
        if ( arr [ i - 1 ] in um and len1 < um [ arr [ i ] - 1 ] ) :
            len1 = um [ arr [ i ] - 1 ]
        if ( arr [ i ] + 1 in um and len1 < um [ arr [ i ] + 1 ] ) :
            len1 = um [ arr [ i ] + 1 ]
        um [ arr [ i ] ] = len1 + 1
        if longLen < um [ arr [ i ] ] :
            longLen = um [ arr [ i ] ]
    return longLen