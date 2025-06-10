def f_gold(n):
        while n & (n-1):
            n = n ^ (n & (n-1))
        return n + 1