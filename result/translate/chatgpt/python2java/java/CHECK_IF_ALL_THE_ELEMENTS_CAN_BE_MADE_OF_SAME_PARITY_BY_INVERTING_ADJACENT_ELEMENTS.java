public static boolean f_gold(int[] a, int n) {
    int count_odd = 0;
    int count_even = 0;
    for (int i = 0; i < n; i++) {
        if ((a[i] & 1) != 0) {
            count_odd += 1;
        } else {
            count_even += 1;
        }
    }
    if (count_odd % 2 != 0 && count_even % 2 != 0) {
        return false;
    } else {
        return true;
    }
}