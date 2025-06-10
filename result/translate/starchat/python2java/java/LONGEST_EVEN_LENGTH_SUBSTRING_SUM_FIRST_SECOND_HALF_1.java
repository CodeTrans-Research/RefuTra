public static int f_gold ( String str ) {
        int n = str. length ( );
        int maxlen = 0;
        int[][] Sum = new int[n][n];
        for ( int i = 0; i < n; i++ ) {
            Sum[i][i] = str.charAt(i) - '0';
        }
        for ( int length = 2; length <= n; length++ ) {
            for ( int i = 0; i < n - length + 1; i++ ) {
                int j = i + length - 1;
                int k = length / 2;
                Sum[i][j] = ( Sum[i][j - k] + Sum[j - k + 1][j] ) ;
                if ( ( length % 2 == 0 && Sum[i][j - k] == Sum[j - k + 1][j] ) && length > maxlen ) {
                    maxlen = length;
                }
            }
        }
        return maxlen;
    }