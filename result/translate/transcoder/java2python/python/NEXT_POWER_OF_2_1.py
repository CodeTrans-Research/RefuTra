def f_gold ( n ) :
    p = 1
    if n and ( n & ( n - 1 ) ) == 0 :
        return n
    while p < n :
        p <<= 1
    return p
