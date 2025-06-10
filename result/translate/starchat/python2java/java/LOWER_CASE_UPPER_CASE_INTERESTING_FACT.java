public static String f_gold ( String in_list ) {
        for ( int i = 0; i < in_list. length(); i++ ) {
            if ( 'a' <= in_list. charAt ( i ) && in_list. charAt ( i ) <= 'z' ) {
                in_list = in_list. replace ( Character. toString ( in_list. charAt ( i ) ), Character. toString ( ( char ) ( in_list. charAt ( i ) - 'a' + 'A' ) ) );
            }
        }
        return in_list;
    }