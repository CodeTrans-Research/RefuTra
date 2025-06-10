public static boolean f_gold(int[] arr, int N) {
    if (N < 3) {
        return false;
    }
    Arrays.sort(arr, 0, N);
    for (int i = 0; i < N - 2; i++) {
        if (arr[i] + arr[i + 1] > arr[i + 2]) {
            return true;
        }
    }
    return false;
}