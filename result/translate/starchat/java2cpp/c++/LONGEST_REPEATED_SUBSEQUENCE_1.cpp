string f_gold ( string str ) {
        int n = str.length();
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i!= j && str[i-1] == str[j-1]) dp[i][j] = 1 + dp[i-1][j-1];
                else dp[i][j] = max(dp[i][j-1], dp[i-1][j]);
            }
        }
        string res = "";
        int i = n, j = n;
        while (i > 0 && j > 0) {
            if (dp[i][j] == dp[i-1][j-1] + 1) {
                res = str[i-1] + res;
                i--;
                j--;
            }
            else if (dp[i][j] == dp[i-1][j]) i--;
            else j--;
        }
        string reverse = "";
        for (int k = res.length() - 1; k >= 0; k--) {
            reverse = res[k] + reverse;
        }
        return reverse;
    }