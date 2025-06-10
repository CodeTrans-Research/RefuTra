def f_gold ( n , x ) :
    f_gold = 0
    i=1 
    while i<=n and i<=x :
        if x / i <= n and x % i == 0 :
            f_gold += 1
        i += 1
    return f_gold

