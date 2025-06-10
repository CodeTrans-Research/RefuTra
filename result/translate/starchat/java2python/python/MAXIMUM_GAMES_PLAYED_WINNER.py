def f_gold(N):
        dp = [0] * (N + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return i - 2