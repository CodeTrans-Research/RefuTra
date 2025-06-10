def f_gold(n):
        res = 0.0
        sign = True
        for i in range(1, n+1):
            if sign:
                sign = False
                res += 1.0 / (i**2)
            else:
                sign = True
                res -= 1.0 / (i**2)
        return res