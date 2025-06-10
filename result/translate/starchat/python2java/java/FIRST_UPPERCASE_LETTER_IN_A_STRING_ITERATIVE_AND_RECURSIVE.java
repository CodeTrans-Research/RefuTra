public static char f_gold ( String str ) {
        for ( int i = 0; i < str.length(); i++ ) {
            if ( str.charAt(i) == Character.toTitleCase(str.charAt(i))) {
                return str.charAt(i);
            }
        }
        return 0;
    }