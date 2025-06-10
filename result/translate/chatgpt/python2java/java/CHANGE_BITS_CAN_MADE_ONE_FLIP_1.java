public static int f_gold(String str) {
    int sum = 0;
    int n = str.length();
    for (int i = 0; i < n; i++) {
        sum += (int) str.charAt(i) - (int) '0';
    }
    return (sum == n - 1 || sum == 1) ? 1 : 0;
}