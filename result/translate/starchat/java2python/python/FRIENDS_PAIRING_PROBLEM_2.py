def f_gold(n):
        if n <= 2:
            return n
        a, b, c = 1, 2, 0
        for i in range(3, n + 1):
            c = b + (i - 1) * a
            a, b = b, c
        return c