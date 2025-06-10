#include <unordered_set>

int f_gold(int arr[], int n) {
    std::unordered_set<int> s;
    for (int i = 0; i < n; i++) {
        if (s.find(arr[i]) != s.end()) return arr[i];
        s.insert(arr[i]);
    }
    return -1;
}