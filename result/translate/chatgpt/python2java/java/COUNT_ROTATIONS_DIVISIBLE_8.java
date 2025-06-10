public static int f_gold(String n) {
    int l = n.length();
    int count = 0;
    if (l == 1) {
        int oneDigit = Integer.parseInt(String.valueOf(n.charAt(0)));
        if (oneDigit % 8 == 0) {
            return 1;
        }
        return 0;
    }
    if (l == 2) {
        int first = Integer.parseInt(String.valueOf(n.charAt(0))) * 10 + Integer.parseInt(String.valueOf(n.charAt(1)));
        int second = Integer.parseInt(String.valueOf(n.charAt(1))) * 10 + Integer.parseInt(String.valueOf(n.charAt(0)));
        if (first % 8 == 0) {
            count += 1;
        }
        if (second % 8 == 0) {
            count += 1;
        }
        return count;
    }
    int threeDigit = 0;
    for (int i = 0; i < (l - 2); i++) {
        threeDigit = (Integer.parseInt(String.valueOf(n.charAt(i))) * 100 + Integer.parseInt(String.valueOf(n.charAt(i + 1))) * 10 + Integer.parseInt(String.valueOf(n.charAt(i + 2)));
        if (threeDigit % 8 == 0) {
            count += 1;
        }
    }
    threeDigit = (Integer.parseInt(String.valueOf(n.charAt(l - 1))) * 100 + Integer.parseInt(String.valueOf(n.charAt(0))) * 10 + Integer.parseInt(String.valueOf(n.charAt(1)));
    if (threeDigit % 8 == 0) {
        count += 1;
    }
    threeDigit = (Integer.parseInt(String.valueOf(n.charAt(l - 2))) * 100 + Integer.parseInt(String.valueOf(n.charAt(l - 1))) * 10 + Integer.parseInt(String.valueOf(n.charAt(0)));
    if (threeDigit % 8 == 0) {
        count += 1;
    }
    return count;
}