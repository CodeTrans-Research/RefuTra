public static int f_gold(String n) {
    int l = n.length();
    if (l == 1) {
        int oneDigit = Integer.valueOf(n.substring(0, 1));
        if (oneDigit % 4 == 0) {
            return 1;
        }
        return 0;
    }
    int count = 0;
    for (int i = 0; i < l - 1; i++) {
        int twoDigit = Integer.valueOf(n.substring(i, i + 1)) * 10 + Integer.valueOf(n.substring(i + 1, i + 2));
        if (twoDigit % 4 == 0) {
            count = count + 1;
        }
    }
    int twoDigit = Integer.valueOf(n.substring(l - 1)) * 10 + Integer.valueOf(n.substring(0, 1));
    if (twoDigit % 4 == 0) {
        count = count + 1;
    }
    return count;
}