def f_gold ( n , p ) :
    x = 0
    while n :
        n //= p
        x += n
    return x