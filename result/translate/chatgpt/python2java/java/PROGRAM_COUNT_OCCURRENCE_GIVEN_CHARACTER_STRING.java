public static int f_gold(String s, char c) {
    int res = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == c) {
            res = res + 1;
        }
    }
    return res;
}