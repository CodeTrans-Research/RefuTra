public static int f_gold ( int n ) {
        int res = 0, x = 0, y = 0;
        while ( x * x < n ) {
            while ( x * x + y * y < n ) {
                res = res + 1;
                y = y + 1;
            }
            x = x + 1;
            y = 0;
        }
        return res;
    }