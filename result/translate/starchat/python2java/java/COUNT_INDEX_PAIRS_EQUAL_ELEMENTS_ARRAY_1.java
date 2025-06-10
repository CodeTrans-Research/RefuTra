public static int f_gold ( int arr [ ] : int n ) {
        HashMap < Integer, Integer > mp = new HashMap < > ( );
        for ( int i = 0; i < n; i ++ ) {
            if ( mp. containsKey ( arr [ i ] ) ) {
                mp. put ( arr [ i ], mp. get ( arr [ i ] ) + 1 );
            } else {
                mp. put ( arr [ i ], 1 );
            }
        }
        int ans = 0;
        for ( int it : mp. values ( ) ) {
            int count = it;
            ans += ( count * ( count - 1 ) ) / 2;
        }
        return ans;
    }