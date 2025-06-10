def f_gold(num):
    if num < 0:
        return False
    sum = 0
    n = 1
    while sum <= num:
        sum += n
        if sum == num:
            return True
        n += 1
    return False