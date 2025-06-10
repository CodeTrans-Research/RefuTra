def f_gold(a, n):
        mn = float("inf")
        sum = 0
        for i in range(n):
            mn = min(a[i], mn)
            sum += a[i]
        return mn * (sum - mn)