public static int f_gold( int N ) {
        return (int) (Math.ceil( Math.log10( N + 1 ) / Math.log10( 2 ) ) - 1 );
    }