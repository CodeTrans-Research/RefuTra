public static int f_gold(int[] p, int i, int j) {
    if (i == j) {
        return 0;
    }
    int _min = Integer.MAX_VALUE;
    for (int k = i; k < j; k++) {
        int count = (f_gold(p, i, k) + f_gold(p, k + 1, j) + p[i - 1] * p[k] * p[j]);
        if (count < _min) {
            _min = count;
        }
    }
    return _min;
}
