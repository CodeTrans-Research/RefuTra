public static int f_gold(int[] a, int n) {
    int zero = 0;
    int two = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            zero += 1;
        }
        if (a[i] == 2) {
            two += 1;
        }
    }
    int cnt = (zero * (zero - 1)) / 2 + (two * (two - 1)) / 2;
    return cnt;
}