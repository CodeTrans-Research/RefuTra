public static int f_gold ( int n ) {
        int result = 0;
        for ( int i = 1 ; i <= 10 ; i++ ) {
            List < Integer > s = new ArrayList < > ( );
            if ( i <= n ) {
                s.add ( i );
                result++;
            }
            while (!s.isEmpty ( ) ) {
                int tp = s.get ( s.size ( ) - 1 );
                s.remove ( s.size ( ) - 1 );
                for ( int j = tp % 10 ; j <= 9 ; j++ ) {
                    int x = tp * 10 + j;
                    if ( x <= n ) {
                        s.add ( x );
                        result++;
                    }
                }
            }
        }
        return result;
    }