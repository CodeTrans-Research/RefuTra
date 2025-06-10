def f_gold(a, n):
        if n == 1:
            return a[0]
        max_neg = -sys.maxsize - 1
        count_neg = 0
        count_zero = 0
        prod = 1
        for i in range(n):
            if a[i] == 0:
                count_zero += 1
            elif a[i] < 0:
                count_neg += 1
                max_neg = max(max_neg, a[i])
            prod += a[i]
        if count_zero == n:
            return 0
        if count_neg % 2 == 1:
            if count_neg == 1 and count_zero > 0 and count_zero + count_neg == n:
                return 0
            prod //= max_neg
        return prod
