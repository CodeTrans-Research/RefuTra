int f_gold(int arr[], int n) {
    unordered_map<int, pair<int, int>> map;
    int d = INT_MIN;
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            map[arr[i] + arr[j]] = make_pair(i, j);
        }
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            int abs_diff = abs(arr[i] - arr[j]);
            if (map.find(abs_diff) != map.end()) {
                pair<int, int> indexes = map[abs_diff];
                if (indexes.first != i && indexes.first != j && indexes.second != i && indexes.second != j) {
                    d = max(d, max(arr[i], arr[j]));
                }
            }
        }
    }
    
    return d;
}