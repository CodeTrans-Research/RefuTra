int f_gold ( int arr [ ], int n ) {
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) mp[arr[i]]++;
    int res = 0;
    for (auto &x : mp) res = max(res, x.second);
    return res;
}