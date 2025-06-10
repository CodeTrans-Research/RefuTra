def f_gold ( arr , n ) :
    for i in range ( 0 , n , 2 ) :
        if i > 0 and arr [ i - 1 ] > arr [ i ] :
            swap ( arr , i - 1 , i )
        if i < n - 1 and arr [ i ] < arr [ i + 1 ] :
            swap ( arr , i , i + 1 )