int f_gold ( int N ) {
  vector <int> dp ( N + 1, 0 );
  dp[0] = 1;
  dp[1] = 2;
  for ( int i = 2; i <= N; i++ ) {
    dp[i] = max ( dp[i-1], dp[i-2] ) + 1;
  }
  return dp[N];
}