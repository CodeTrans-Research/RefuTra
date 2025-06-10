def f_gold(n):
        res = 1
        for r in range(1, n + 1):
            res = (res * (n + 1 - r)) // r
            res *= res
        return res