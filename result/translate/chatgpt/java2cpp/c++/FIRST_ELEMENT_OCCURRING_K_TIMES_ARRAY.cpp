#include <unordered_map>

int f_gold(int arr[], int n, int k) {
    std::unordered_map<int, int> count_map;
    for (int i = 0; i < n; i++) {
        int a = 0;
        if (count_map.find(arr[i]) != count_map.end()) {
            a = count_map[arr[i]];
        }
        count_map[arr[i]] = a + 1;
    }
    for (int i = 0; i < n; i++) {
        if (count_map[arr[i]] == k) {
            return arr[i];
        }
    }
    return -1;
}