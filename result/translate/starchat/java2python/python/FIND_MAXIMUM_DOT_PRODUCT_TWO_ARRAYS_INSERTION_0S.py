def f_gold(A, B, m, n):
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i, m + 1):
                dp[i][j] = max((dp[i - 1][j - 1] + A[j - 1] * B[i - 1]) if j > i - 1 else dp[i][j - 1], dp[i][j])
        return dp[n][m]