def f_gold(n):
    x = 0
    yCount = 0
    res = 0
    while yCount * yCount < n:
        yCount += 1
    while yCount != 0:
        res += yCount
        x += 1
        while yCount != 0 and (x * x + (yCount - 1) * (yCount - 1) >= n):
            yCount -= 1
    return res