def f_gold(s):
    n = len(s)
    sub_count = n * (n + 1) // 2
    arr = [None] * sub_count
    index = 0
    for i in range(n):
        for length in range(1, n - i + 1):
            arr[index] = s[i:i + length]
            index += 1
    arr.sort()
    res = ""
    for i in range(sub_count):
        res += arr[i]
    return res