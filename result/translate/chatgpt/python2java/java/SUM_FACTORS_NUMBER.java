public static int f_gold(int n) {
    int result = 0;
    for (int i = 2; i <= (int) Math.sqrt(n); i++) {
        if (n % i == 0) {
            if (i == (n / i)) {
                result = result + i;
            } else {
                result = result + (i + n / i);
            }
        }
    }
    return (result + n + 1);
}