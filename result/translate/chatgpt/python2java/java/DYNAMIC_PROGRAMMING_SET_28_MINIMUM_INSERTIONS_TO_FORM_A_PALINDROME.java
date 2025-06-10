public static int f_gold(char[] str, int l, int h) {
    if (l > h) {
        return Integer.MAX_VALUE;
    }
    if (l == h) {
        return 0;
    }
    if (l == h - 1) {
        return str[l] == str[h] ? 0 : 1;
    }
    if (str[l] == str[h]) {
        return f_gold(str, l + 1, h - 1);
    } else {
        return Math.min(f_gold(str, l, h - 1), f_gold(str, l + 1, h)) + 1;
    }
}