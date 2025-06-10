def f_gold ( n ) :
    res = 0
    x=0 
    while x*x<n :
        y=0 
        while x*x+y*y<n :
            res += 1
            y += 1
        x += 1
    return res

