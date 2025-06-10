def f_gold(s):
        sum = 0
        for n in range(1, s + 1):
            sum += n * n * n
            if sum == s:
                return n
        return -1