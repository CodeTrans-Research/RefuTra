int f_gold ( int A [ ], int B [ ], int m, int n ) {
  int **dp = new int *[n + 1];
  for (int i = 0; i <= n; i++)
    dp[i] = new int[m + 1]();
  for (int i = 1; i <= n; i++)
    for (int j = i; j <= m; j++)
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
  for (int i = n; i > 0; i--)
    delete[] dp[i];
  delete[] dp;
  return dp[n][m];
}
