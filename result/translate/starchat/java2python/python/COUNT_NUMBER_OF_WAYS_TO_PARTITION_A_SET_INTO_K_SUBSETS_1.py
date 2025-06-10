def f_gold(n, k):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(k + 1):
                if j == 0 or i == j:
                    dp[i][j] = 0
                elif j == 1:
                    dp[i][j] = i
                else:
                    dp[i][j] = j * dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[n][k]