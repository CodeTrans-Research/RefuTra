def f_gold(a, n):
    min_val = a[0]
    for i in range(1, len(a)):
        if a[i] < min_val:
            min_val = a[i]
    return (n - 1) * min_val