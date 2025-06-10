public static int f_gold ( int n ) {
        int num = n, dec_value = 0, base = 1;
        while (num > 0) {
            int last_digit = num % 10;
            num /= 10;
            dec_value += last_digit * base;
            base *= 8;
        }
        return dec_value;
    }