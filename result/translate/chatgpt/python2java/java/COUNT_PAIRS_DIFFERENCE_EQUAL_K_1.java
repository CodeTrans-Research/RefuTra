public static int f_gold(int[] arr, int n, int k) {
    int count = 0;
    Arrays.sort(arr);
    int l = 0;
    int r = 0;
    while (r < n) {
        if (arr[r] - arr[l] == k) {
            count += 1;
            l += 1;
            r += 1;
        } else if (arr[r] - arr[l] > k) {
            l += 1;
        } else {
            r += 1;
        }
    }
    return count;
}