public static char f_gold ( String strA, String strB ) {
        int res = 0;
        for ( int i = 0; i < strA.length(); i++ ) {
            res = res ^ strA.charAt(i);
        }
        for ( int i = 0; i < strB.length(); i++ ) {
            res = res ^ strB.charAt(i);
        }
        return (char)res;
    }