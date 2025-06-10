public static int f_gold ( String str ) {
        int one_count = 0, zero_count = 0, n = str. length ();
        for ( int i = 0 ; i < n ; i++ ) {
            if ( str. charAt ( i ) == '1' ) one_count ++;
            else zero_count ++;
        }
        if ( one_count % 2 == 0 ) return zero_count;
        return one_count;
    }