def f_gold(x, y):
    res1 = int(math.log(y) / math.log(x))
    res2 = math.log(y) / math.log(x)
    return res1 == res2