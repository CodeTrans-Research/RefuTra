def f_gold(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            dp[i][j] = False
    
    dp[0][0] = True
    
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                if j < m and (s1[i].upper() == s2[j]):
                    dp[i + 1][j + 1] = True
                if not s1[i].isupper():
                    dp[i + 1][j] = True
                    
    return dp[n][m]