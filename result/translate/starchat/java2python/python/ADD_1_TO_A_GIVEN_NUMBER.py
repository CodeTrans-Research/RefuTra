def f_gold(x):
        m = 1
        while (x & m) >= 1:
            x = x ^ m
            m = m << 1
        return x