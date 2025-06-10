  int f_gold ( String str ) {
        int N = str. length ();
        int[][] cps = new int[N + 2][N + 2];
        for ( int i = 0; i < N; i++ ) {
            cps[i][i] = 1;
        }
        for (int L=2;L<N+1;L++){
            for ( int i = 0; i < N; i++ ) {
                int k = L + i - 1;
                if ( k < N ) {
                    if ( str. charAt(i) == str. charAt(k) ) {
                        cps[i][k] = cps[i][k - 1] + cps[i + 1][k] + 1;
                    } else {
                        cps[i][k] = cps[i][k - 1] + cps[i + 1][k] - cps[i + 1][k - 1];
                    }
                }
            }
        }
        return cps[0][N - 1];
    }
