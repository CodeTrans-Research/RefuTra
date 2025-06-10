def f_gold(x):
        i = 1
        fact = 1
        while i < x:
            fact = fact * i
            if fact % x == 0:
                return i
            i += 1