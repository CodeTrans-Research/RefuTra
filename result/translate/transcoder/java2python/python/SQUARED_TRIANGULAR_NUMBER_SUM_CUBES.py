def f_gold ( s ) :
    sum = 0
    for n in range ( 1 , s ) :
        sum += n ** 2 * n ** 2
        if sum == s :
            return n
