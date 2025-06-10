def f_gold(a, n, m):
    for i in range(n):
        sum1 = 0
        sum2 = 0
        for j in range(m):
            sum1 += a[i][j]
            sum2 += a[j][i]
        if sum1 == sum2:
            return True
    return False