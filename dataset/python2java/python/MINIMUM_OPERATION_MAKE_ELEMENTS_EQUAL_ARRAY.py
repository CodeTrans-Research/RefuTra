def f_gold ( arr , n ) :
    Hash = defaultdict ( lambda : 0 )
    for i in range ( 0 , n ) :
        Hash [ arr [ i ] ] += 1
    max_count = 0
    for i in Hash :
        if max_count < Hash [ i ] :
            max_count = Hash [ i ]
    return n - max_count