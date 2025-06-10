def f_gold(n):
        while n > 0:
            n = (n & (n - 1)) + 1
        return n