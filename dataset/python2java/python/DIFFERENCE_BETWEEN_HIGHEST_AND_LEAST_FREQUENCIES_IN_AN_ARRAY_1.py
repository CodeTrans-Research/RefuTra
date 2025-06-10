def f_gold ( arr , n ) :
    mp = defaultdict ( lambda : 0 )
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    max_count = 0
    min_count = n
    for key , values in mp.items ( ) :
        max_count = max ( max_count , values )
        min_count = min ( min_count , values )
    return max_count - min_count