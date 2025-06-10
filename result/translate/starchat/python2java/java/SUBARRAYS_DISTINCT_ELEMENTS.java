public static int f_gold ( int arr [ ] : int n ) {
        int s [ ] = new int [ 100000 ];
        int j = 0;
        int ans = 0;
        for ( int i = 0; i < n; i++ ) {
            while ( j < n && ( arr [ j ] not in s ) ) {
                s [ j ] = arr [ j ];
                j++;
            }
            ans += ( ( j - i ) * ( j - i + 1 ) ) / 2;
            s [ i ] = 0;
        }
        return ans;
    }