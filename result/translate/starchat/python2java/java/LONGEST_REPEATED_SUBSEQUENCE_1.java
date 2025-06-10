public static String f_gold ( String str ) {
        int n = str. length ();
        int[][] dp = new int[n + 1][n + 1];
        for ( int i = 1; i <= n; i++ ) {
            for ( int j = 1; j <= n; j++ ) {
                if ( i!= j && str.charAt(i - 1) == str.charAt(j - 1) ) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
        StringBuilder res = new StringBuilder();
        int i = n, j = n;
        while ( i > 0 && j > 0 ) {
            if ( dp[i][j] == dp[i - 1][j - 1] + 1 ) {
                res.append(str.charAt(i - 1));
                i--;
                j--;
            } else if ( dp[i][j] == dp[i -}