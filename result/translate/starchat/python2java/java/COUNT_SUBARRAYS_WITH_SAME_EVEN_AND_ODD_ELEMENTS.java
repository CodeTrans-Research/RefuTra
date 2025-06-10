public static int f_gold ( int arr [ ], int n ) {
        int difference = 0, ans = 0;
        int hash_positive [ ] = new int [ n + 1 ];
        int hash_negative [ ] = new int [ n + 1 ];
        hash_positive [ 0 ] = 1;
        for ( int i = 0 ; i < n ; i++ ) {
            if ( ( arr [ i ] & 1 ) == 1 ) difference++;
            else difference--;
            if ( difference < 0 ) ans += hash_negative [ -difference ];
            else ans += hash_positive [ difference ];
            if ( difference >= 0 ) hash_positive [ difference ]++;
            else hash_negative [ -difference ]++;
        }
        return ans;
    }