def f_gold(x):
    res = 0
    count = 0
    count += 1
    if count == 1:
        res = x
    else:
        r = random.Random()
        i = r.randint(0, count-1)
        if i == count - 1:
            res = x
    return res