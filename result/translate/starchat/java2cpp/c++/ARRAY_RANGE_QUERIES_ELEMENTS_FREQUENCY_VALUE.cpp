int f_gold ( int start, int end, int arr [ ] ) {
    unordered_map<int, int> mp;
    for (int i = start; i <= end; i++) mp[arr[i]]++;
    int count = 0;
    for (auto &x : mp) if (x.second == 1) count++;
    return count;
}