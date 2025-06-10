int f_gold(int A[], int B[], int m, int n) {
    int** dp = new int*[n + 1];
    for (int i = 0; i < n + 1; i++) {
        dp[i] = new int[m + 1];
    }
    
    for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < m + 1; j++) {
            dp[i][j] = 0;
        }
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= m; j++) {
            dp[i][j] = max(dp[i - 1][j - 1] + (A[j - 1] * B[i - 1]), dp[i][j - 1]);
        }
    }
    
    return dp[n][m];
}