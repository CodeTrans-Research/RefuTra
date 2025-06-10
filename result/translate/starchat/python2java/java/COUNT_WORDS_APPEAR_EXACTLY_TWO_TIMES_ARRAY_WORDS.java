public static int f_gold ( String stri, int n ) {
        Map < Character, Integer > m = new HashMap < > ( );
        for ( int i = 0; i < n; i++ ) {
            char ch = stri.charAt ( i );
            m.put ( ch, m.getOrDefault ( ch, 0 ) + 1 );
        }
        int res = 0;
        for ( int i : m.values ( ) ) {
            if ( i == 2 ) {
                res++;
            }
        }
        return res;
    }