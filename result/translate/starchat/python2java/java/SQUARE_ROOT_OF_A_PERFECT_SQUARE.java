public static double f_gold ( double n ) {
        double x = n, y = 1;
        double e = 1e-6;
        while ( Math.abs ( x - y ) > e ) {
            x = ( x + y ) / 2;
            y = n / x;
        }
        return x;
    }