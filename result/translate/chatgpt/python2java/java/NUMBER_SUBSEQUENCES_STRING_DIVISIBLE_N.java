public int f_gold(String str, int n) {
    int l = str.length();
    int[][] dp = new int[l][n];
    dp[0][(str.charAt(0) - '0') % n] += 1;
    for (int i = 1; i < l; i++) {
        dp[i][(str.charAt(i) - '0') % n] += 1;
        for (int j = 0; j < n; j++) {
            dp[i][j] += dp[i - 1][j];
            dp[i][(j * 10 + (str.charAt(i) - '0')) % n] += dp[i - 1][j];
        }
    }
    return dp[l - 1][0];
}