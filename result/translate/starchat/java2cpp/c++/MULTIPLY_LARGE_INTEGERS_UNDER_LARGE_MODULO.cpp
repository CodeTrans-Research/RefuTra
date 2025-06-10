long f_gold ( long a, long b, long mod ) {
    long res = 0;
    a = a % mod;
    while (b > 0) {
        if ((b & 1) > 0) {
            res = (res + a) % mod;
        }
        a = (2 * a) % mod;
        b = b >> 1;
    }
    return res;
}