def f_gold(n):
    ans = 0
    temp = 0
    num = 0
    i = 1
    while i <= n and temp < n:
        temp = i - 1
        num = 1
        while temp < n:
            if temp + i <= n:
                ans += (i * num)
            else:
                ans += ((n - temp) * num)
            temp += i
            num += 1
        i += 1
    return ans