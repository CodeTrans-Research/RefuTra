def f_gold ( n ) :
    x , y_count , res = 0 , 0 , 0
    for y_count in range ( 0 , y_count * y_count < n ) :
        pass
    while y_count != 0 :
        res += y_count
        x += 1
        while y_count != 0 and ( x * x + ( y_count - 1 ) * ( y_count - 1 ) >= n ) :
            y_count -= 1
    return res
