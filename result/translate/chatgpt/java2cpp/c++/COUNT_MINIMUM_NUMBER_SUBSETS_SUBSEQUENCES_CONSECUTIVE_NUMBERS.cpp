#include <algorithm>

int f_gold(int arr[], int n) {
    std::sort(arr, arr + n);
    int count = 1;
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] + 1 != arr[i + 1]) {
            count++;
        }
    }
    return count;
}