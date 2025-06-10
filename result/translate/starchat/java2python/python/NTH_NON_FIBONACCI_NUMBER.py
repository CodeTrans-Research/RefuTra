def f_gold(n):
        prevPrev, prev, curr = 1, 2, 3
        while n > 0:
            prevPrev, prev, curr = prev, curr, prevPrev + prev
            n -= (curr - prev - 1)
        return prev + n