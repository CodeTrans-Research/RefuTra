public static int f_gold(int[] arr, int n) {
    int[] lis = new int[n];
    Arrays.fill(lis, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j] && lis[i] < lis[j] + 1) {
                lis[i] = lis[j] + 1;
            }
        }
    }
    int maximum = 0;
    for (int i = 0; i < n; i++) {
        maximum = Math.max(maximum, lis[i]);
    }
    return maximum;
}