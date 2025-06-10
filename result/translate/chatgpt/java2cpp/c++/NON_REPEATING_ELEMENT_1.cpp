int f_gold(int arr[], int n) {
    unordered_map<int, int> m;
    for (int i = 0; i < n; i++) {
        if (m.find(arr[i]) != m.end()) {
            m[arr[i]] = m[arr[i]] + 1;
        } else {
            m[arr[i]] = 1;
        }
    }
    for (int i = 0; i < n; i++)
        if (m[arr[i]] == 1) return arr[i];
    return -1;
}