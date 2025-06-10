public static String f_gold(String s) {
    char[] chars = s.toCharArray();
    int n = s.length();
    for (int i = 1; i < n; i++) {
        if (chars[i] == chars[i - 1]) {
            chars[i] = 'a';
            while (chars[i] == chars[i - 1] || (i + 1 < n && chars[i] == chars[i + 1])) {
                chars[i] += 1;
            }
            i += 1;
        }
    }
    return new String(chars);
}