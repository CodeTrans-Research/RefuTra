def f_gold ( a , arr_size ) :
    lo = 0
    hi = arr_size - 1
    mid , temp = 0 , 0
    while mid <= hi :
        try :
            temp = a [ mid ]
            a [ lo ] , a [ mid ] = a [ mid ] , temp
            lo += 1
            mid += 1
            break
        except IndexError :
            mid += 1
    return a [ lo ] , a [ mid ]