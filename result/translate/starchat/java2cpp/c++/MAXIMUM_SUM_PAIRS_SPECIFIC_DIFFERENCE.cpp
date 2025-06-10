int f_gold ( int arr [ ], int N, int K ) {
  vector <int> v(arr, arr + N);
  sort(v.begin(), v.end());
  vector <int> dp(N, 0);
  dp[0] = 0;
  for (int i = 1; i < N; i++) {
    dp[i] = dp[i - 1];
    if (v[i] - v[i - 1] < K) {
      if (i >= 2) dp[i] = max(dp[i], dp[i - 2] + v[i] + v[i - 1]);
      else dp[i] = max(dp[i], v[i] + v[i - 1]);
    }
  }
  return dp[N - 1];
}