int f_gold(int arr[], int N, int K) {
    std::sort(arr, arr + N);
    int *dp = new int[N];
    dp[0] = 0;
    
    for (int i = 1; i < N; i++) {
        dp[i] = dp[i - 1];
        if (arr[i] - arr[i - 1] < K) {
            if (i >= 2) dp[i] = std::max(dp[i], dp[i - 2] + arr[i] + arr[i - 1]);
            else dp[i] = std::max(dp[i], arr[i] + arr[i - 1]);
        }
    }
    
    return dp[N - 1];
}