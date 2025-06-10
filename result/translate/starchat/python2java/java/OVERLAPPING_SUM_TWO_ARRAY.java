public static int f_gold ( int A [ ], int B [ ], int n ) {
        HashMap < Integer, Integer > Hash = new HashMap < > ( );
        for ( int i = 0 ; i < n ; i++ ) {
            Hash.put ( A [ i ], Hash.getOrDefault ( A [ i ], 0 ) + 1 );
            Hash.put ( B [ i ], Hash.getOrDefault ( B [ i ], 0 ) + 1 );
        }
        int Sum = 0;
        for ( int x : Hash.keySet ( ) ) {
            if ( Hash.get ( x ) == 1 ) {
                Sum += x;
            }
        }
        return Sum;
    }