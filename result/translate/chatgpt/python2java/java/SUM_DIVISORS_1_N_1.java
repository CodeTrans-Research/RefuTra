public static int f_gold(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += (int) (n / i) * i;
    }
    return (int) sum;
}