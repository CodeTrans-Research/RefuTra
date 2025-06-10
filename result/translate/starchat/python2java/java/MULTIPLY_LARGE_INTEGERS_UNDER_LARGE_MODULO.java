public static int f_gold ( int a, int b, int mod ) {
        int res = 0;
        a = a % mod;
        while (b > 0) {
            if ((b & 1) == 1) {
                res = (res + a) % mod;
            }
            a = (2 * a) % mod;
            b = b >> 1;
        }
        return res;
    }