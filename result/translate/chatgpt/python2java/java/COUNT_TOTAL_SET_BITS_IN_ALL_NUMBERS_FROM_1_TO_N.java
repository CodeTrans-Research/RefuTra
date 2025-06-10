public static int f_gold(int n) {
    int i = 0;
    int ans = 0;
    while ((1 << i) <= n) {
        int k = 0;
        int change = 1 << i;
        for (int j = 0; j < n + 1; j++) {
            ans += k;
            if (change == 1) {
                k = k == 0 ? 1 : 0;
                change = 1 << i;
            } else {
                change -= 1;
            }
        }
        i += 1;
    }
    return ans;
}