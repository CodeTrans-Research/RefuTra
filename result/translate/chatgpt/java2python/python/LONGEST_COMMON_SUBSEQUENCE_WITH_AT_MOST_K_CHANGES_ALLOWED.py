def f_gold(dp, arr1, n, arr2, m, k):
    if k < 0:
        return -10000000
    if n < 0 or m < 0:
        return 0
    ans = dp[n][m][k]
    if ans != -1:
        return ans
    try:
        ans = max(f_gold(dp, arr1, n - 1, arr2, m, k), f_gold(dp, arr1, n, arr2, m - 1, k))
        if arr1[n - 1] == arr2[m - 1]:
            ans = max(ans, 1 + f_gold(dp, arr1, n - 1, arr2, m - 1, k))
        ans = max(ans, 1 + f_gold(dp, arr1, n - 1, arr2, m - 1, k - 1))
    except Exception as e:
        pass
    return ans