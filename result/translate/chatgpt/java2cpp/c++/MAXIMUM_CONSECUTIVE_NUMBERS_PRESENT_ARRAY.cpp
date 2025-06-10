int f_gold(int arr[], int n) {
    unordered_set<int> S;
    for (int i = 0; i < n; i++) {
        S.insert(arr[i]);
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (S.find(arr[i]) != S.end()) {
            int j = arr[i];
            while (S.find(j) != S.end()) {
                j++;
            }
            ans = max(ans, j - arr[i]);
        }
    }
    return ans;
}