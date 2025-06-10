public static int f_gold(int[] a, int n) {
    Arrays.sort(a, 0, n);
    int sum = 0;
    boolean flag = false;
    int len = 0;
    int i = 0;
    while (i < n - 1) {
        if ((a[i] == a[i + 1] || a[i] - a[i + 1] == 1) && !flag) {
            flag = true;
            len = a[i + 1];
            i++;
        } else if ((a[i] == a[i + 1] || a[i] - a[i + 1] == 1) && flag) {
            sum += a[i + 1] * len;
            flag = false;
            i++;
        }
        i++;
    }
    return sum;
}