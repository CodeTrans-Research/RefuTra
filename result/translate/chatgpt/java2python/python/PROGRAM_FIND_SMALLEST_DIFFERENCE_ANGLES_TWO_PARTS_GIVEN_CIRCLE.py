def f_gold(arr, n):
    l = 0
    sum = 0
    ans = 360
    for i in range(n):
        sum += arr[i]
        while sum >= 180:
            ans = min(ans, 2 * abs(180 - sum))
            sum -= arr[l]
            l += 1
        ans = min(ans, 2 * abs(180 - sum))
    return ans