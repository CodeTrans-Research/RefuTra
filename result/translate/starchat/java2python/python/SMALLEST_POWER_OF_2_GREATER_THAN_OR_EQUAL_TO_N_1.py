def f_gold(n):
        if n > 0 and (n & (n - 1)) == 0:
            return n
        p = 1
        while p < n:
            p = p << 1
        return p