public static int f_gold(int[] arr, int n) {
    Arrays.sort(arr, 0, n);
    return arr[n-1];
}