static int f_gold(int arr[], int n) {
    int[] mpis = new int[n];
    for (int i = 0; i < n; i++) {
        mpis[i] = arr[i];
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j] && mpis[i] < (mpis[j] * arr[i])) {
                mpis[i] = mpis[j] * arr[i];
            }
        }
    }
    int max_val = mpis[0];
    for (int i = 1; i < n; i++) {
        max_val = Math.max(max_val, mpis[i]);
    }
    return max_val;
}