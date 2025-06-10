bool f_gold(int a[], int n) {
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        if (mp.find(a[i]) != mp.end()) {
            mp[a[i]]++;
        } else {
            mp[a[i]] = 1;
        }
    }
    for (auto x : mp) {
        if (x.second >= n / 2) {
            return true;
        }
    }
    return false;
}