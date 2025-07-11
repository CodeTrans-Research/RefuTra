public static int f_gold(int[] arr, int n) {
    int total_sum = 0;
    for (int i = 0; i < n; i++) {
        total_sum += arr[i];
    }
    int leftsum = 0;
    for (int i = 0; i < n; i++) {
        total_sum -= arr[i];
        if (leftsum == total_sum) {
            return i;
        }
        leftsum += arr[i];
    }
    return -1;
}