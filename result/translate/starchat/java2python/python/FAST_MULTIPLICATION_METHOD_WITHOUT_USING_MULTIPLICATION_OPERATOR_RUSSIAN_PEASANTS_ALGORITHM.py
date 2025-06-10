def f_gold(a: int, b: int) -> int:
        res = 0
        while b > 0:
            if b & 1:
                res += a
            a = a << 1
            b = b >> 1
        return res