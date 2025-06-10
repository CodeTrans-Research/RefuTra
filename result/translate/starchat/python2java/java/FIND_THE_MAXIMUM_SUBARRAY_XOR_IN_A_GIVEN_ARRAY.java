public static int f_gold ( int arr [ ], int n ) {
        int ans = Integer.MIN_VALUE;
        for ( int i = 0 ; i < n ; i++ ) {
            int curr_xor = 0;
            for ( int j = i ; j < n ; j++ ) {
                curr_xor ^= arr [ j ];
                ans = Math.max ( ans, curr_xor );
            }
        }
        return ans;
    }