def f_gold ( n ) :
    a , b , c = 1 , 2 , 0
    if n <= 2 :
        return n
    for i in range ( 3 , n ) :
        c = b + ( i - 1 ) * a
        a , b , c = b , c , c
    return c
