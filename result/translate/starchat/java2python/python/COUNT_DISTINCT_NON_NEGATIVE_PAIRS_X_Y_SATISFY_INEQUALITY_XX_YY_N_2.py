def f_gold(n):
        res = 0
        for x in range(n):
            for y in range(n):
                if x * x + y * y < n:
                    res += 1
        return res