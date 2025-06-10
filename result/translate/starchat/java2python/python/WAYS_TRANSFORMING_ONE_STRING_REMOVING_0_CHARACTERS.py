def f_gold(a, b):
        n = len(a)
        m = len(b)
        if m == 0:
            return 1
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    if j == 0:
                        dp[i][j] = (a[j] == b[i]) * 1
                    else:
                        if a[j] == b[i]:
                            dp[i][j] = dp[i][j - 1] + 1
                        else:
                            dp[i][j] = dp[i][j - 1]
                else:
                    if j == 0:
                        if a[j] == b[i - 1]:
                            dp[i][j] = dp[i - 1][j] + 1
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        if a[j] == b[i - 1] and b[i]