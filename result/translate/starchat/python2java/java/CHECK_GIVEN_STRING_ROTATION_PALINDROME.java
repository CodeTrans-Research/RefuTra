public static boolean f_gold ( String s ) {
        int l = 0, h = s. length () - 1;
        while ( h > l ) {
            if ( s. charAt ( l )!= s. charAt ( h ) ) return false;
            l++;
            h--;
        }
        return true;
    }