int f_gold(string str) {
    int n = str.length();
    int **dp = new int*[n + 1];
    for (int i = 0; i <= n; i++) {
        dp[i] = new int[n + 1]();
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (str[i - 1] == str[j - 1] && i != j) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
            }
        }
    }
    
    return dp[n][n];
}
