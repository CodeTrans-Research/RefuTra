def f_gold(r, R, r1, x1, y1):
    dis = int((x1**2 + y1**2)**0.5)
    return (dis - r1 >= R) and (dis + r1 <= r)