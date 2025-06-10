int f_gold ( int n, int a, int b, int c ) {
    vector<int> dp(n+10,-1);
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i]!=-1) {
            if (i+a<=n) dp[i+a] = max(dp[i]+1,dp[i+a]);
            if (i+b<=n) dp[i+b] = max(dp[i]+1,dp[i+b]);
            if (i+c<=n) dp[i+c] = max(dp[i]+1,dp[i+c]);
        }
    }
    return dp[n];
}