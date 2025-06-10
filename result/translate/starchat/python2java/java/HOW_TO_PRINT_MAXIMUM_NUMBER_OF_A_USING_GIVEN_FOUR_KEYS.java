public static int f_gold ( int N ) {
        if ( N <= 6 ) return N;
        int[] screen = new int[N];
        for ( int n = 1; n < 7; n++ ) screen[n - 1] = n;
        for ( int n = 7; n < N + 1; n++ ) {
            screen[n - 1] = Math.max( 2 * screen[n - 4], Math.max( 3 * screen[n - 5], 4 * screen[n - 6] ) );
        }
        return screen[N - 1];
    }