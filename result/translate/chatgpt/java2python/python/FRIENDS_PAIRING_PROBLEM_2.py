def f_gold(n):
    a = 1
    b = 2
    c = 0
    if n <= 2:
        return n
    for i in range(3, n+1):
        c = b + (i - 1) * a
        a = b
        b = c
    return c