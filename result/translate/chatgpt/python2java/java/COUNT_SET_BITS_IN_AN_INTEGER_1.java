public static int f_gold(int n) {
    if (n == 0) {
        return 0;
    } else {
        return (n & 1) + f_gold(n >> 1);
    }
}