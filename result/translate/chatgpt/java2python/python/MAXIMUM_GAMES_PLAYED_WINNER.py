def f_gold(N):
    dp = [0] * N
    dp[0] = 1
    dp[1] = 2
    i = 2
    while (dp[i - 1] + dp[i - 2]) <= N:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1
    return i - 2