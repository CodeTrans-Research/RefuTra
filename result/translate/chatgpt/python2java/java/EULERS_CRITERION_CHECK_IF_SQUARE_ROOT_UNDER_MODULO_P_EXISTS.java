public static boolean f_gold(int n, int p) {
    n = n % p;
    for (int x = 2; x < p; x++) {
        if ((x * x) % p == n) {
            return true;
        }
    }
    return false;
}