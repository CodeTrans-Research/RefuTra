public static double f_gold ( int n ) {
        double res = 0, i = 1;
        boolean sign = true;
        while (n > 0) {
            n--;
            if (sign) {
                sign = false;
                res += (i + 1) / (i + 2);
                i += 2;
            } else {
                sign = true;
                res -= (i + 1) / (i + 2);
                i += 2;
            }
        }
        return res;
    }