def f_gold ( n ) :
    res = 1
    i=n 
    while i>-1 :
        if i == 0 or i == 1 :
            return res
        else :
            res *= i
        i=i-2
    return res

