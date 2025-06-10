int f_gold ( string a, string b ) {
  int n = a.length(), m = b.length();
  vector<vector<int>> dp(m+1, vector<int>(n+1));
  for (int i = 0; i < m+1; i++) {
    for (int j = 0; j < n+1; j++) {
      if (i == 0) {
        if (j == 0) {
          dp[i][j] = (a[j] == b[i])? 1 : 0;
        } else if (a[j] == b[i]) {
          dp[i][j] = dp[i][j-1] + 1;
        } else {
          dp[i][j] = dp[i][j-1];
        }
      } else if (j == 0) {
        dp[i][j] = dp[i-1][j];
      } else if (a[j] == b[i]) {
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1];
      } else {
        dp[i][j] = dp[i][j-1];
      }
    }
  }
  return dp[m][n];
}