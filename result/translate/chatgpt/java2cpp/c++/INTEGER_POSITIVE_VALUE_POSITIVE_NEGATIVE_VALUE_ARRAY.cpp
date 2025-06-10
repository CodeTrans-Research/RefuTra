#include <unordered_map>

int f_gold(int arr[], int n) {
    std::unordered_map<int, int> hash;
    int maximum = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0)
            hash[abs(arr[i])] = (hash[abs(arr[i])] == 0 ? 0 : hash[abs(arr[i])]) - 1;
        else
            hash[abs(arr[i])] = (hash[abs(arr[i])] == 0 ? 0 : hash[abs(arr[i])]) + 1;
    }
    
    for (int i = 0; i < n; i++)
        if (hash[arr[i]] > 0)
            return arr[i];
    
    return -1;
}