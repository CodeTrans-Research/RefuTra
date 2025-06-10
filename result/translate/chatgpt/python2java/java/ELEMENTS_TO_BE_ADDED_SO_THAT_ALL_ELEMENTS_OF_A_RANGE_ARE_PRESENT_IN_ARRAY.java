public static int f_gold(int[] arr, int n) {
    int count = 0;
    int[] newArr = Arrays.copyOfRange(arr, 0, n);
    Arrays.sort(newArr);
    for (int i = 0; i < n - 1; i++) {
        if (newArr[i] != newArr[i + 1] && newArr[i] != newArr[i + 1] - 1) {
            count += newArr[i + 1] - newArr[i] - 1;
        }
    }
    return count;
}