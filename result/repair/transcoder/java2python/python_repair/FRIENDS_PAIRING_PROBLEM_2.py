def f_gold ( n ) :
    a , b , c = 1 , 2 , 0
    if n <= 2 :
        return n
    i=3 
    while i<n+1 :
        c = b + ( i - 1 ) * a
        a , b , c = b , c , c
        i += 1
    return c

