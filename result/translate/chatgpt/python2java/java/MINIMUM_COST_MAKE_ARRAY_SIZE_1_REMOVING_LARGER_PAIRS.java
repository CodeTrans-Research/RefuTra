public static int f_gold(int[] a, int n) {
    int min = a[0];
    for (int i = 1; i < a.length; i++) {
        min = Math.min(min, a[i]);
    }
    return (n - 1) * min;
}