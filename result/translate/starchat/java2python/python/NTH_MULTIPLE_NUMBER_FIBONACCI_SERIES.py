def f_gold(k, n):
        f1, f2, f3 = 0, 1, 0
        for i in range(2, 10000):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            if f2 % k == 0:
                return n * i
        return 0