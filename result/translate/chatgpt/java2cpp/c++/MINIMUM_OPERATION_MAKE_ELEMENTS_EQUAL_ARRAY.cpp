int f_gold(int arr[], int n) {
    unordered_map<int, int> hash;
    for (int i = 0; i < n; i++) {
        if (hash.find(arr[i]) != hash.end()) {
            hash[arr[i]]++;
        } else {
            hash[arr[i]] = 1;
        }
    }
    int max_count = 0;
    for (auto i : hash) {
        if (max_count < i.second) {
            max_count = i.second;
        }
    }
    return (n - max_count);
}