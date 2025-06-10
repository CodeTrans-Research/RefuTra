def f_gold ( n ) :
    res = 0
    for x in range ( 0 , n * x ) :
        for y in range ( 0 , x * x + y * y ) :
            res += 1
    return res
