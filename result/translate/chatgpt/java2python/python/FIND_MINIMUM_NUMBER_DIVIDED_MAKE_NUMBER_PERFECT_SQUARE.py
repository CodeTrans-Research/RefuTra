def f_gold(n):
    count = 0
    ans = 1
    while n % 2 == 0:
        count += 1
        n //= 2
    if count % 2 == 1:
        ans *= 2
    i = 3
    while i <= int(n ** 0.5):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count % 2 == 1:
            ans *= i
        i += 2
    if n > 2:
        ans *= n
    return ans