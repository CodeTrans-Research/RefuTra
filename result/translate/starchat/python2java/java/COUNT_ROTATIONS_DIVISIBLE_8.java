public static int f_gold ( String n ) {
        int l = n. length ();
        int count = 0;
        if (l == 1) {
            int oneDigit = Integer.parseInt (n.substring (0, 1));
            if (oneDigit % 8 == 0) {
                return 1;
            }
            return 0;
        }
        if (l == 2) {
            int first = (int) (n.substring (0, 1)) * 10 + (int) (n.substring (1, 2));
            int second = (int) (n.substring (1, 2)) * 10 + (int) (n.substring (0, 1));
            if (first % 8 == 0) {
                count++;
            }
            if (second % 8 == 0) {
                count++;
            }
            return count;
        }
        int threeDigit = 0;
        for (int i = 0; i < l - 2; i++) {
            threeDigit = (int) (n.substring (i, i + 3)) * 100 + (int) (n.substring (i + 1, i + 2)) * 10 + (int) (n.substring (i + 2, i + 3));
            if (threeDigit % 8 == 0) {
                count++;
            }
        }
        threeDigit = (int) (n.substring (l - 1, l)) * 100 + (int) (n.substring (0, 1)) * 10 + (int) (n.substring (1, 2));
        if (threeDigit % 8 == 0) {
            count++;
        }
        threeDigit = (int) (n.substring (l - 2, l - 1)) * 100 + (int) (n.substring (l - 1, l)) * 10 + (int) (n.substring (0, 1));
        if (threeDigit % 8 == 0) {
            count++;
        }
        return count;
    }