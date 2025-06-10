def f_gold(n):
        for sum, i in zip(accumulate(range(1, n, 2)), count(1)):
            if sum == n:
                return True
        return False