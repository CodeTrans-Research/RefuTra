def f_gold(a, b):
        if a < b:
            a, b = b, a
        res = 0
        while b > 0:
            res += a // b
            a, b = b, a % b
        return res