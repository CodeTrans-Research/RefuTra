def f_gold(x1, y1, x2, y2, r1, r2):
        dist_sq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        rad_sum_sq = (r1 + r2) * (r1 + r2)
        if dist_sq == rad_sum_sq:
            return 1
        elif dist_sq > rad_sum_sq:
            return -1
        else:
            return 0