public static int f_gold ( int A [ ], int B [ ], int n ) {
        Set < Integer > mp = new HashSet < > ( );
        int result = 0, curr_sum = 0, curr_begin = 0;
        for ( int i = 0 ; i < n ; i++ ) {
            while ( A [ i ]!= mp.iterator ( ) ) {
                mp.remove ( A [ curr_begin ] );
                curr_sum -= B [ curr_begin ];
                curr_begin++;
            }
            mp.add ( A [ i ] );
            curr_sum += B [ i ];
            result = Math.max ( result, curr_sum );
        }
        return result;
    }