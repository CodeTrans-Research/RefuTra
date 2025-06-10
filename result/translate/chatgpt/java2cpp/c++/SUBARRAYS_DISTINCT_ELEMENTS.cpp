int f_gold(int arr[], int n) {
    vector<int> s;
    int j = 0;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        while (j < n && find(s.begin(), s.end(), arr[j]) == s.end()) {
            s.push_back(arr[j]);
            j++;
        }
        ans += ((j - i) * (j - i + 1)) / 2;
        s.erase(remove(s.begin(), s.end(), arr[i]), s.end());
    }
    return ans;
}