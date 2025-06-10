public static boolean f_gold ( int[][] m ) {
        for ( int i = 0; i < m.length; i++ ) {
            int sm = 0;
            for ( int j = 0; j < m[0].length; j++ ) {
                sm += m[i][j];
            }
            if ( sm!= 1 ) {
                return false;
            }
        }
        return true;
    }