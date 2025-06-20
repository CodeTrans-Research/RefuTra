def f_gold(n, x, y):
    arr = [False] * (n + 1)
    if x <= n:
        arr[x] = True
    if y <= n:
        arr[y] = True
    result = 0
    for i in range(min(x, y), n + 1):
        if arr[i]:
            if i + x <= n:
                arr[i + x] = True
            if i + y <= n:
                arr[i + y] = True
            result += 1
    return result