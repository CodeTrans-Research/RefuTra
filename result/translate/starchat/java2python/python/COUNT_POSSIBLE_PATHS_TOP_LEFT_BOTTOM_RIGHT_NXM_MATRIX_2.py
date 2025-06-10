def f_gold(m, n):
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]