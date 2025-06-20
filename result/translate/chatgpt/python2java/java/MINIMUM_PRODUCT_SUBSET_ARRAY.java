public static int f_gold(int[] a, int n) {
    if (n == 1) {
        return a[0];
    }
    int max_neg = Integer.MIN_VALUE;
    int min_pos = Integer.MAX_VALUE;
    int count_neg = 0;
    int count_zero = 0;
    int prod = 1;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            count_zero++;
            continue;
        }
        if (a[i] < 0) {
            count_neg++;
            max_neg = Math.max(max_neg, a[i]);
        }
        if (a[i] > 0) {
            min_pos = Math.min(min_pos, a[i]);
        }
        prod *= a[i];
    }
    if (count_zero == n || (count_neg == 0 && count_zero > 0)) {
        return 0;
    }
    if (count_neg == 0) {
        return min_pos;
    }
    if ((count_neg % 2) == 0 && count_neg != 0) {
        prod = prod / max_neg;
    }
    return prod;
}