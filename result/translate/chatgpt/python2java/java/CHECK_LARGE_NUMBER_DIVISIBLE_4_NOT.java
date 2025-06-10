public boolean f_gold(String str) {
    int n = str.length();
    if (n == 0) {
        return false;
    }
    if (n == 1) {
        return ((str.charAt(0) - '0') % 4 == 0);
    }
    int last = Integer.parseInt(str.substring(n - 1));
    int second_last = Integer.parseInt(str.substring(n - 2, n - 1));
    return ((second_last * 10 + last) % 4 == 0);
}