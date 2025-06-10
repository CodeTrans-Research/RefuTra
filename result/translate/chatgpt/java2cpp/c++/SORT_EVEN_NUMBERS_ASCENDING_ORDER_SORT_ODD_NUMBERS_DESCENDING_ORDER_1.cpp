void f_gold(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        if ((arr[i] & 1) != 0) {
            arr[i] *= -1;
        }
    }
    
    std::sort(arr, arr + n);
    
    for (int i = 0; i < n; i++) {
        if ((arr[i] & 1) != 0) {
            arr[i] *= -1;
        }
    }
}