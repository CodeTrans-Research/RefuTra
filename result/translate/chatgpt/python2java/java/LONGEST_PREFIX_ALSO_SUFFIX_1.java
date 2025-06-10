public static int f_gold (String s ) {
    int n = s.length();
    int[] lps = new int[n];
    int l = 0;
    int i = 1;
    while (i < n) {
        if (s.charAt(i) == s.charAt(l)) {
            l = l + 1;
            lps[i] = l;
            i = i + 1;
        } else {
            if (l != 0) {
                l = lps[l - 1];
            } else {
                lps[i] = 0;
                i = i + 1;
            }
        }
    }
    int res = lps[n - 1];
    if (res > n / 2) {
        return n / 2;
    } else {
        return res;
    }
}