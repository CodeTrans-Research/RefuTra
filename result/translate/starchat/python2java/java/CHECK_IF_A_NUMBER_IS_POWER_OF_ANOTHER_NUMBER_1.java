public static int f_gold ( int x, int y ) {
        double res1 = Math.log ( y ) / Math.log ( x );
        double res2 = Math.log ( y ) - Math.log ( x ) * res1;
        return ( int ) ( res1 == res2 )? 1 : 0;
    }