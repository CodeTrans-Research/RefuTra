public static int f_gold ( int[][] mat, int r, int c ) {
        int result = 0;
        for ( int i = 0; i < r; i++ ) {
            int j = 0;
            while ( j < c - 1 && mat[i][j + 1] <= mat[i][j] ) {
                j++;
            }
            if ( j == c - 1 ) {
                result++;
            }
            for ( j = c - 1; j > 0; j-- ) {
                if ( mat[i][j - 1] <= mat[i][j] ) {
                    break;
                }
            }
            if ( j == 0 && c > 1 ) {
                result++;
            }
        }
        return result;
    }