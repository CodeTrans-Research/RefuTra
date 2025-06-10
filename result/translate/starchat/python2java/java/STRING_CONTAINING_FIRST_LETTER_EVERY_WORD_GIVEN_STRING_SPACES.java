public static String f_gold ( String str ) {
        StringBuilder result = new StringBuilder ();
        boolean v = true;
        for ( int i = 0; i < str. length ( ); i++ ) {
            if ( str. charAt ( i ) =='' ) {
                v = true;
            } else if ( str. charAt ( i )!='' && v == true ) {
                result. append ( str. charAt ( i ) );
                v = false;
            }