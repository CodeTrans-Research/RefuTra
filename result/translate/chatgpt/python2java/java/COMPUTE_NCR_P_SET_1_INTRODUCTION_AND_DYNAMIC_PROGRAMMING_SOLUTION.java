public static int f_gold(int n, int r, int p) {
    int[] C = new int[r + 1];
    C[0] = 1;
    for (int i = 1; i < n + 1; i++) {
        for (int j = Math.min(i, r); j > 0; j--) {
            C[j] = (C[j] + C[j - 1]) % p;
        }
    }
    return C[r];
}