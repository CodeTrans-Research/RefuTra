bool f_gold ( string s ) {
        int n = s. length ( );
        if ( n >= 10 ) return true;
        for ( int i = 1; i < n; i++ ) {
            for ( int j = i + 1; j < n; j++ ) {
                for ( int k = j + 1; k < n; k++ ) {
                    string s1 = s. substr ( 0, i ), s2 = s. substr ( i, j ), s3 = s. substr ( j, k ), s4 = s. substr ( k, n );
                    if ( s1!= s2 && s1!= s3 && s1!= s4 && s2!= s3 && s2!= s4 && s3!= s4 ) return true;
                }
            }
        }
        return false;
    }