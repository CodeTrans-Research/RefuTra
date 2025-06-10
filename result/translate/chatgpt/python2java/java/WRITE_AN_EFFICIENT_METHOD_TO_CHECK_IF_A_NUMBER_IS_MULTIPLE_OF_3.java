public static int f_gold(int n) {
    int odd_count = 0;
    int even_count = 0;
    if (n < 0) {
        n = -n;
    }
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return 0;
    }
    while (n != 0) {
        if ((n & 1) == 1) {
            odd_count += 1;
        }
        if ((n & 2) == 1) {
            even_count += 1;
        }
        n = n >> 2;
    }
    return f_gold(Math.abs(odd_count - even_count));
}