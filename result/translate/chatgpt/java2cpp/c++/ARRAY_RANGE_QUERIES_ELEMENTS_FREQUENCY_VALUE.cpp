int f_gold(int start, int end, int arr[]) {
    std::unordered_map<int, int> mp;
    for(int i = start; i <= end; i++) {
        mp[arr[i]] = mp[arr[i]] == 0 ? 1 : mp[arr[i]] + 1;
    }

    int count = 0;
    for(auto entry : mp) {
        if(entry.first == entry.second) {
            count++;
        }
    }

    return count;
}