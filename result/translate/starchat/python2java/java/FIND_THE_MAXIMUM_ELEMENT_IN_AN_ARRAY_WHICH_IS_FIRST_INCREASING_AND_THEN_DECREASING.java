public static int f_gold ( int arr [ ], int low, int high ) {
        int max = arr [ low ];
        for ( int i = low; i <= high; i++ ) {
            if ( arr [ i ] > max ) {
                max = arr [ i ];
            }
        }
        return max;
    }