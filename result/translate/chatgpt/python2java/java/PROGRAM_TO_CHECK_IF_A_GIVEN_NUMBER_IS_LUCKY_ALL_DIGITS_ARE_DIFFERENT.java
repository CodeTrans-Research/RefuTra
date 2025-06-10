public static boolean f_gold(int n) {
    int[] ar = new int[10];
    while (n > 0) {
        int digit = (int)Math.floor(n % 10);
        if (ar[digit] != 0) {
            return false;
        }
        ar[digit] = 1;
        n = (int)(n / 10);
    }
    return true;
}