public static int f_gold(int a, int b, int k) {
    int p = (int) Math.pow(a, b);
    int count = 0;
    while (p > 0 && count < k) {
        int rem = p % 10;
        count = count + 1;
        if (count == k) {
            return rem;
        }
        p = p / 10;
    }
    return 0;
}