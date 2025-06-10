def f_gold(n):
    if n % 2 != 0:
        return 0
    res = 1
    i = 2
    while i <= int(n ** 0.5):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n //= i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
        i += 1
    if n >= 2:
        res *= (1 + n)
    return res