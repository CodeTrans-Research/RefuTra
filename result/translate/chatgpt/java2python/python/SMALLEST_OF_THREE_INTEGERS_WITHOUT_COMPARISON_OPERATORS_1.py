def f_gold(x, y, z):
    if (y // x) == 0:
        return y if (y // z) == 0 else z
    return x if (x // z) == 0 else z