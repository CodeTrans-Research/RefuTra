def f_gold ( arr , n ) :
    left_max = [ int ( x ) for x in arr ]
    right_min = int ( arr [ - 1 ] )
    for i in range ( 1 , n ) :
        left_max [ i ] = max ( left_max [ i - 1 ] , arr [ i - 1 ] )
    right_min = sys.maxsize
    for i in range ( n - 1 , - 1 , - 1 ) :
        if (left_max[i]<arr[i] and right_min>arr[i]) :
            return i
        right_min = min ( right_min , arr [ i ] )
    return - 1

