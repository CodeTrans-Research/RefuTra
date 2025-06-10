def f_gold(x, y, z):
        if (y // x) == 0:
            return (y // z) == 0 and y or z
        return (x // z) == 0 and x or z