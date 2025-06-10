public static int f_gold ( int n ) {
        int[][] C = new int[n + 2][n + 2];
        for ( int i = 0; i < n + 2; i++ ) {
            for ( int j = 0; j < n + 2; j++ ) {
                if ( j == 0 || j == i ) {
                    C[i][j] = 1;
                } else {
                    C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
                }
            }
        }
        int sum = 0;
        for ( int i = 0; i < n + 1; i++ ) {
            sum += C[n][i];
        }
        return sum;
    }