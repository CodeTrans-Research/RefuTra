def f_gold(a, n):
    mn = float('inf')
    sum_val = 0
    for i in range(n):
        mn = min(a[i], mn)
        sum_val += a[i]
    return mn * (sum_val - mn)