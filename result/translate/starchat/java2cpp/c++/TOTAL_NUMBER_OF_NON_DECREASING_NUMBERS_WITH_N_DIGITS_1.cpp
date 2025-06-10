long f_gold ( int n ) {
    long res = 1;
    for (int i = 1; i <= n; i++) {
        res = res * (10 + n - i) / i;
    }
    return res;
}