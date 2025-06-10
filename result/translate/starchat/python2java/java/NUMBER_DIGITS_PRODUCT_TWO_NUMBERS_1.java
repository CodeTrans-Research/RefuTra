public static int f_gold ( int a, int b ) {
        if ( a == 0 || b == 0 ) {
            return 1;
        }
        return (int) ( Math.floor ( Math.log10 ( Math.abs ( a ) ) ) + Math.floor ( Math.log10 ( Math.abs ( b ) ) ) ) + 1;
    }