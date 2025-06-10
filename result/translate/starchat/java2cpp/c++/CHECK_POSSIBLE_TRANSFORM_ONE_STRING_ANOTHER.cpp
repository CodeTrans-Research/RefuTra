bool f_gold ( string s1, string s2 ) {
        int n = s1. length ( );
        int m = s2. length ( );
        vector<vector<bool>> dp (n + 1, vector<bool> (m + 1, false));
        for ( int i = 0; i <= n; i++ ) dp[i][0] = true;
        for ( int j = 0; j <= m; j++ ) dp[0][j] = false;
        for ( int i = 1; i <= n; i++ ) {
            for ( int j = 1; j <= m; j++ ) {
                if ( s1[i - 1] == s2[j - 1] ||!isupper(s1[i - 1]) ) dp[i][j] = dp[i - 1][j - 1];
                if ( dp[i][j] &&!isupper(s1[i - 1]) ) dp[i][j] = true;
            }
        }
        return dp[n][m];
    }