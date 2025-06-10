def f_gold(n):
    count = 0
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n = n // 2
    i = 3
    while i <= int(n ** 0.5):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n = n // i
        i += 2
    if n > 2:
        count += 1
    return count