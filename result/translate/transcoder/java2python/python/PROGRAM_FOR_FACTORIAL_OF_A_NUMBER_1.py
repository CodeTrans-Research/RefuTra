def f_gold ( n ) :
    res , i = 1 , 1
    for i in range ( 2 , n + 1 ) :
        res *= i
    return res
