int f_gold(int a[], int n) {
    unordered_set<int> s;
    for (int i = 0; i < n; i++) {
        s.insert(a[i]);
    }
    int arr_sum = 0;
    for (int i = 0; i < n; i++) {
        arr_sum += a[i];
    }
    int set_sum = 0;
    for (auto i : s) {
        set_sum += i;
    }
    return (3 * set_sum - arr_sum) / 2;
}