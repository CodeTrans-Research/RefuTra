public static boolean f_gold(int n) {
    while ((n / 100) > 0) {
        int last_digit = n % 10;
        n = n / 10;
        n += last_digit * 3;
    }
    return (n % 29 == 0);
}