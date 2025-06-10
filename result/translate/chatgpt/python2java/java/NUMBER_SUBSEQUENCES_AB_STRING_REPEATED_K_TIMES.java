public static int f_gold(String s, int K) {
    int n = s.length();
    int c1 = 0;
    int c2 = 0;
    int C = 0;
    for (int i = 0; i < n; i++) {
        if (s.charAt(i) == 'a') {
            c1 += 1;
        }
        if (s.charAt(i) == 'b') {
            c2 += 1;
            C += c1;
        }
    }
    return C * K + (int) (K * (K - 1) / 2) * c1 * c2;
}