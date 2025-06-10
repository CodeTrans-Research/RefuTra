def f_gold(ar, n):
    res = 0
    ar.sort()
    i = 0
    while i < n:
        count = 1
        while i < n - 1:
            if ar[i] == ar[i + 1]:
                count += 1
            else:
                break
            i += 1
        res = max(res, count)
        i += 1
    return res