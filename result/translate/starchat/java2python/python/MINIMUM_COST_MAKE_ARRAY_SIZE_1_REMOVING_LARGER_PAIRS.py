def f_gold(a, n):
        min = a[0]
        for i in range(1, n):
            if a[i] < min:
                min = a[i]
        return (n - 1) * min