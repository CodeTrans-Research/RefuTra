def f_gold ( arr , n , k ) :
    mp = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    for key , values in mp.items ( ) :
        if values > 2 * k :
            return False
    return True