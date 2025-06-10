public static boolean f_gold(int num) {
    if (num < 0) {
        return false;
    }
    int sum = 0, n = 1;
    while (sum <= num) {
        sum = sum + n;
        if (sum == num) {
            return true;
        }
        n += 1;
    }
    return false;
}