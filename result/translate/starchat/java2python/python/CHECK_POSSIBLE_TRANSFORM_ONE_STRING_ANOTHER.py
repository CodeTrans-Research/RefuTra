def f_gold(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and (s2[j - 1].isupper() or s1[i - 1] == s2[j - 1])
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1].isupper() or s1[i - 1] == s2[j - 1])
                else:
                    dp[i][j] = dp[i - 1][j] and (s1[i - 1] == s2[j - 1]) or (dp[i][j - 1] and (s