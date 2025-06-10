def f_gold ( arr , n ) :
    maxv = max(arr)
    minv = min(arr)
    mp = { i : 0 for i in range ( minv, maxv+1 ) }
    for i in range ( n ) :
        mp [ arr [ i ] ] += 1
    res = 0
    for key , value in mp.items ( ) :
        res = max ( res , value )
    return res