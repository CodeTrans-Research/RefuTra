def f_gold(p):
        checkNumber = (2 ** p) - 1
        nextval = 4 % checkNumber
        for i in range(1, p - 1):
            nextval = (nextval * nextval - 2) % checkNumber
        return nextval == 0