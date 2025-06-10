public static boolean f_gold(String str) {
    int n = str.length();
    int i;
    for (i = 0; i < n; i++) {
        if (str.charAt(i) != 'a') {
            break;
        }
    }
    if (i * 2 != n) {
        return false;
    }
    for (int j = i; j < n; j++) {
        if (str.charAt(j) != 'b') {
            return false;
        }
    }
    return true;
}