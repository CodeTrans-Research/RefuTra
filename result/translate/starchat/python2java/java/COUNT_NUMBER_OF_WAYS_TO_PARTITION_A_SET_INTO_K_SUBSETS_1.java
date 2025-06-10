public static int f_gold ( int n, int k ) {
        int[][] dp = new int[n + 1][k + 1];
        for ( int i = 0; i <= n; i++ ) {
            for ( int j = 0; j <= k; j++ ) {
                if ( j == 0 || i == j ) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = ( j * dp[i - 1][j] + dp[i - 1][j - 1] ) % 1000000007;
                }
            }
        }
        return dp[n][k];
    }