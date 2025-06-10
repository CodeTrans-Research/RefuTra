def f_gold(arr, n):
    S = set()
    for i in range(n):
        S.add(arr[i])
    ans = 0
    for i in range(n):
        if arr[i] in S:
            j = arr[i]
            while j in S:
                j += 1
            ans = max(ans, j - arr[i])
    return ans