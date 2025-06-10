def f_gold(k):
    cur = (k * (k - 1)) + 1
    sum = 0
    while k > 0:
        sum += cur
        cur += 2
        k -= 1
    return sum