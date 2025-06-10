def f_gold(a, b, mod):
    res = 0
    a %= mod
    while b > 0:
        if b & 1 > 0:
            res = (res + a) % mod
        a = (2 * a) % mod
        b >>= 1
    return res