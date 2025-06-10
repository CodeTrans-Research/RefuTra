public static int f_gold ( int[][] input, int n ) {
        int[][] row = new int[n][n];
        int[][] col = new int[n][n];
        for ( int j = 0; j < n; j++ ) {
            boolean isEndless = true;
            for ( int i = n - 1; i >= 0; i-- ) {
                if ( input[i][j] == 0 ) {
                    isEndless = false;
                }
                col[i][j] = isEndless;
            }
        }
        for ( int i = 0; i < n; i++ ) {
            boolean isEndless = true;
            for ( int j = n - 1; j >= 0; j-- ) {
                if ( input[i][j] == 0 ) {
                    isEndless = false;
                }
                row[i][j] = isEndless;
            }
        }
        int ans = 0;
        for ( int i = 0; i < n; i++ ) {
            for ( int j = 1; j < n; j++ ) {
                if ( row[i][j] && col[i][j] ) {
                    ans++;
                }
            }
        }
        return ans;
    }