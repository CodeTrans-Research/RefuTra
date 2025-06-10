public static int f_gold ( int limit ) {
        if ( limit < 2 ) {
            return 0;
        }
        int ef1 = 0, ef2 = 2, sm = ef1 + ef2;
        while ( ef2 <= limit ) {
            int ef3 = 4 * ef2 + ef1;
            if ( ef3 > limit ) {
                break;
            }
            ef1 = ef2;
            ef2 = ef3;
            sm = sm + ef2;
        }
        return sm;
    }