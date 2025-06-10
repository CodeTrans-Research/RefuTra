def f_gold(n):
        if n > 0 and (n & (n - 1)) == 0:
            return n
        count = 0
        while n!= 0:
            n = n >> 1
            count += 1
        return 1 << count