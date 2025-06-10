def f_gold(n, k, x):
        dp = [0] * 109
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = (k - 2) * dp[i - 1] + (k - 1) * dp[i - 2]
        return (x == 1 and (k - 1) * dp[n - 2]) or dp[n - 1]