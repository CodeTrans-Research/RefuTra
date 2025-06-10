public static int f_gold(int[] arr, int n) {
    int[] x = arr.clone();
    Arrays.sort(x);
    int count = 1;
    for (int i = 0; i < n - 1; i++) {
        if ((x[i] + 1) != x[i + 1]) {
            count = count + 1;
        }
    }
    return count;
}