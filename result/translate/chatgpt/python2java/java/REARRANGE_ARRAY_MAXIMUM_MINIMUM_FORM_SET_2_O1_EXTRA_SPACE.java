public void f_gold(int arr[], int n) {
    int max_idx = n - 1;
    int min_idx = 0;
    int max_elem = arr[n - 1] + 1;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            arr[i] += (arr[max_idx] % max_elem) * max_elem;
            max_idx -= 1;
        } else {
            arr[i] += (arr[min_idx] % max_elem) * max_elem;
            min_idx += 1;
        }
    }
    for (int i = 0; i < n; i++) {
        arr[i] = arr[i] / max_elem;
    }
}