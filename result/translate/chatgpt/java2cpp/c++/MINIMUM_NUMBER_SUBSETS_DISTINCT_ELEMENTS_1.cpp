#include <unordered_map>

int f_gold(int arr[], int n) {
    std::unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        mp[arr[i]] = (mp[arr[i]] == 0) ? 1 : mp[arr[i]] + 1;
    }
    
    int res = 0;
    for (auto const& entry : mp) {
        res = std::max(res, entry.second);
    }
    
    return res;
}