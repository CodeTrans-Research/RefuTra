public static int f_gold(int n) {
    int p = 1;
    if ((n & (n - 1)) == 0) {
        return n;
    }
    while (p < n) {
        p <<= 1;
    }
    return p;
}