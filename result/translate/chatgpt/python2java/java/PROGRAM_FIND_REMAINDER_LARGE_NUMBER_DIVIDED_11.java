public static int f_gold(String str) {
    int ln = str.length();
    int rem = 0;
    for (int i = 0; i < ln; i++) {
        int num = rem * 10 + Integer.parseInt(String.valueOf(str.charAt(i)));
        rem = num % 11;
    }
    return rem;
}