public static String f_gold ( String s ) {
        int n = s. length ( );
        int sub_count = ( n * ( n + 1 ) ) / 2;
        String [ ] arr = new String [ sub_count ];
        int index = 0;
        for ( int i = 0; i < n; i++ ) {
            for ( int j = 1; j < n - i + 1; j++ ) {
                arr [ index ] = s.substring ( i, i + j );
                index++;
            }
        }
        Arrays. sort ( arr );
        String res = "";
        for ( int i = 0; i < sub_count; i++ ) {
            res += arr [ i ];
        }
        return res;
    }