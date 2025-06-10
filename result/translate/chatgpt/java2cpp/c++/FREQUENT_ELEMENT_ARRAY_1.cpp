int f_gold(int arr[], int n) {
    unordered_map<int, int> hp;
    for (int i = 0; i < n; i++) {
        int key = arr[i];
        if (hp.find(key) != hp.end()) {
            int freq = hp[key];
            freq++;
            hp[key] = freq;
        } else {
            hp[key] = 1;
        }
    }
    int max_count = 0, res = -1;
    for (auto val : hp) {
        if (max_count < val.second) {
            res = val.first;
            max_count = val.second;
        }
    }
    return res;
}