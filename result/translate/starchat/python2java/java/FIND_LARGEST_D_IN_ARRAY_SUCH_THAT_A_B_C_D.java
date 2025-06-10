public static int f_gold ( String S, int n ) {
        boolean found = false;
        S = S.substring ( 0, n );
        Arrays.sort ( S.toCharArray ( ) );
        for ( int i = n - 1 ; i >= 0 ; i -- ) {
            for ( int j = 0 ; j < n ; j ++ ) {
                if ( i == j ) continue;
                for ( int k = j + 1 ; k < n ; k ++ ) {
                    if ( i == k ) continue;
                    for ( int l = k + 1 ; l < n ; l ++ ) {
                        if ( i == l ) continue;
                        if ( S.charAt ( i ) == ( S.charAt ( j ) + S.charAt ( k ) + S.charAt ( l ) ) ) {
                            found = true;
                            return S.charAt ( i );
                        }
                    }
                }
            }
        }
        if (!found ) return - 1;
    }