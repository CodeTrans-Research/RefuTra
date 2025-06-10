bool f_gold(int arr[], int n, int k) {
    unordered_map<int, int> hash;
    for (int i = 0; i < n; i++) {
        if (hash.find(arr[i]) == hash.end()) hash[arr[i]] = 0;
        hash[arr[i]]++;
    }
    for (auto x : hash) if (x.second > 2 * k) return false;
    return true;
}