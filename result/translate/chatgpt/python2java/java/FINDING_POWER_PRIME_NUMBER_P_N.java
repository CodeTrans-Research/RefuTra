public static int f_gold(int n, int p) {
    int ans = 0;
    int temp = p;
    while (temp <= n) {
        ans += (int)(n / temp);
        temp = temp * p;
    }
    return ans;
}