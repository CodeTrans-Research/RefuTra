public static int f_gold ( int[][] mat, int n ) {
        int tot_energy = 0;
        for ( int i = 0; i < n; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                int q = mat[i][j] / n;
                int i_des = q;
                int j_des = mat[i][j] - ( n * q );
                tot_energy += Math.abs( i_des - i ) + Math.abs( j_des - j );
            }
        }
        return tot_energy;
    }