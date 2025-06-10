public static int f_gold(int n) {
    int count = 0;
    if (n % 2 == 0) {
        count = count + 1;
        while (n % 2 == 0) {
            n = n / 2;
        }
    }
    int i = 3;
    while (i <= (int)Math.sqrt(n)) {
        if (n % i == 0) {
            count = count + 1;
            while (n % i == 0) {
                n = n / i;
            }
        }
        i = i + 2;
    }
    if (n > 2) {
        count = count + 1;
    }
    return count;
}