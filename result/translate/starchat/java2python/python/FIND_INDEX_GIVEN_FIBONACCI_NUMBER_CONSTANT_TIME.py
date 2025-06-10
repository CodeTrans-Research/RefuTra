def f_gold(n):
        if n <= 1:
            return n
        a, b, c = 0, 1, 1
        res = 1
        while c < n:
            c = a + b
            res += 1
            a, b = b, c
        return res