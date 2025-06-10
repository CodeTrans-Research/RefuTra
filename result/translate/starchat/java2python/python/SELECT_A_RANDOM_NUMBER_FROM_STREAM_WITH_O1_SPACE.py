def f_gold(x):
        res = 0
        count = 0
        count += 1
        if count == 1:
            res = x
        else:
            import random
            i = random.randint(0, count - 1)
            if i == count - 1:
                res = x
        return res