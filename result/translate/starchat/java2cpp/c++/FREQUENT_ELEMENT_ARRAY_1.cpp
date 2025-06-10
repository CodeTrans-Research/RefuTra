int f_gold ( int arr [ ], int n ) {
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int key = arr[i];
        if (mp.find(key)!= mp.end()) {
            mp[key]++;
        } else {
            mp[key] = 1;
        }
    }
    int max_count = 0, res = -1;
    for (auto it : mp) {
        if (max_count < it.second) {
            max_count = it.second;
            res = it.first;
        }
    }
    return res;
}