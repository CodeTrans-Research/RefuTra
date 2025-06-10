def f_gold ( arr , n ) :
    min_xor = 999999
    val = 0
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            val = arr [ i ] ^ arr [ j ]
            min_xor = min ( min_xor , val )
    return min_xor