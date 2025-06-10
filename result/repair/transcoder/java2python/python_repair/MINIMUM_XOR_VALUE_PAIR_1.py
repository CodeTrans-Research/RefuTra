def f_gold ( arr , n ) :
    arr = np.array ( arr , dtype = np.int32 )
    arr = np.sort ( arr )
    min_xor = sys.maxsize
    val = 0
    for i in range ( n - 1 ) :
        val = arr [ i ] ^ arr [ i + 1 ]
        min_xor = min ( min_xor , val )
    return min_xor
