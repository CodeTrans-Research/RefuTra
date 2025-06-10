public static boolean f_gold ( String str ) {
        int zeros = 0, ones = 0;
        for ( int i = 0; i < str.length(); i++ ) {
            char ch = str.charAt(i);
            if ( ch == '0' ) zeros++;
            else ones++;
        }
        return zeros == 1 || ones == 1;
    }