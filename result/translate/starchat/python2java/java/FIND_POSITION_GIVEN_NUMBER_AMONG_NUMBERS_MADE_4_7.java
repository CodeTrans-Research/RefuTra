public static int f_gold(String n) {
        int i = 0, j = n.length();
        int pos = 0;
        while (i < j) {
            if (n.charAt(i) == '4') {
                pos = pos * 2 + 1;
            } else if (n.charAt(i) == '7') {
                pos = pos * 2 + 2;
            }
            i++;
        }
        return pos;
    }