def f_gold(s):
    sum = 0
    n = 1
    while sum < s:
        sum += n * n * n
        if sum == s:
            return n
        n += 1
    return -1