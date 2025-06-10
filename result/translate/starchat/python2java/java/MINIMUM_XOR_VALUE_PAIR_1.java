public static int f_gold ( int arr [ ], int n ) {
        Arrays.sort ( arr, 0, n );
        int minXor = Integer.MAX_VALUE;
        for ( int i = 0 ; i < n - 1 ; i++ ) {
            minXor = Math.min ( minXor, arr [ i ] ^ arr [ i + 1 ] );
        }
        return minXor;
    }