def f_gold(n):
        count = 0
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count