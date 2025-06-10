double f_gold(int n) {
        double res = 0;
        bool sign = true;
        for (int i = 1; i <= n; i++) {
            if (sign) {
                sign =!sign;
                res += 1.0 / (i * (i + 1));
            } else {
                sign =!sign;
                res -= 1.0 / (i * (i + 1));
            }
        }
        return res;
    }