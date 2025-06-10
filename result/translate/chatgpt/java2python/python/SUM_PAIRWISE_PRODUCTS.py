def f_gold(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            sum = sum + i * j
    return sum