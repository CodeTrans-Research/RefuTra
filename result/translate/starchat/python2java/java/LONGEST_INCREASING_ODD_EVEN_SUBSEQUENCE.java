public static int f_gold ( int arr [ ] : int n ) {
        int lioes [ ] = new int [ n ];
        int maxLen = 0;
        for ( int i = 0; i < n; i++ ) {
            lioes [ i ] = 1;
        }
        int i = 1;
        while ( i < n ) {
            for ( int j = 0; j < i; j++ ) {
                if ( arr [ i ] > arr [ j ] && ( arr [ i ] + arr [ j ] ) % 2!= 0 && lioes [ i ] < lioes [ j ] + 1 ) {
                    lioes [ i ] = lioes [ j ] + 1;
                }
            }
            i++;
        }
        for ( int i = 0; i < n; i++ ) {
            if ( maxLen < lioes [ i ] ) {
                maxLen = lioes [ i ];
            }
        }
        return maxLen;
    }