def f_gold(n):
    count = 0
    curr = 1
    while True:
        sum_val = 0
        x = curr
        while x > 0:
            sum_val += x % 10
            x = x // 10
        if sum_val == 10:
            count += 1
        if count == n:
            return curr
        curr += 1