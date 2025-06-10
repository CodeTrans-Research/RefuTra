def f_gold(n):
    sum_value = 0
    i = 1
    while sum_value < n:
        sum_value += i
        if sum_value == n:
            return True
        i += 2
    return False