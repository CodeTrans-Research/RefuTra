def f_gold(y, x):
    import math
    if (math.log(y) / math.log(2)) < x:
        return y
    if x > 63:
        return y
    return y % (1 << int(x))