def f_gold(n):
        count = 0
        for i in range(5, int(n**0.5) + 1, 5):
            count += n // i
        return count