int f_gold(int arr[], int n) {
    std::sort(arr, arr + n);
    return arr[n - 1] + arr[n - 2] + arr[n - 3];
}