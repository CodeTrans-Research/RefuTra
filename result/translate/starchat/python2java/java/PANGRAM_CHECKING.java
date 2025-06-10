public static boolean f_gold ( String s ) {
        boolean [] List = new boolean [ 26 ];
        for ( int i = 0; i < 26; i++ ) List [ i ] = false;
        for ( int i = 0; i < s. length ( ); i++ ) {
            char c = s. charAt ( i );
            if ( 'A' <= c && c <= 'Z' ) List [ c - 'A' ] = true;
            else if ( 'a' <= c && c <= 'z' ) List [ c - 'a' ] = true;
        }
        for ( boolean ch : List ) if (!ch ) return false;
        return true;
    }