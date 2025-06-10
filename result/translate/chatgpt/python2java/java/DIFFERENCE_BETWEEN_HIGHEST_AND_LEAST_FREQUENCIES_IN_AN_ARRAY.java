public static int f_gold(int[] arr, int n) {
    Arrays.sort(arr);
    int count = 0;
    int max_count = 0;
    int min_count = n;
    for (int i = 0; i < (n - 1); i++) {
        if (arr[i] == arr[i + 1]) {
            count++;
            continue;
        } else {
            max_count = Math.max(max_count, count);
            min_count = Math.min(min_count, count);
            count = 0;
        }
    }
    return max_count - min_count;
}