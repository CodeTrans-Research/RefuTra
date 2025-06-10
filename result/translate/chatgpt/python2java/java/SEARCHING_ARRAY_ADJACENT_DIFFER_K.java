public static int f_gold(int[] arr, int n, int x, int k) {
    int i = 0;
    while (i < n) {
        if (arr[i] == x) {
            return i;
        }
        i = i + Math.max(1, (int) (Math.abs(arr[i] - x) / k));
    }
    System.out.println("number is not present!");
    return -1;
}