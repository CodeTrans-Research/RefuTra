def f_gold ( arr1 , arr2 , n ) :
    for i in range ( n ) :
        if arr1 [ i ] != arr2 [ i ] :
            return i
    return n
