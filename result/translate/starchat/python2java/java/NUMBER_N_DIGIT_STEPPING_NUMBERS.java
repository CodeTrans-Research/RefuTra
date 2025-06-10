public static int f_gold ( int n ) {
        int[][] dp = new int[n + 1][10];
        for (int i = 0; i < 10; i++) {
            dp[1][i] = 1;
        }
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i - 1][j + 1];
                } else if (j == 9) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]);
                }
            }
        }
        int sum = 0;
        for (int j = 0; j < 10; j++) {
            sum = sum + dp[n][j];
        }
        return sum;
    }