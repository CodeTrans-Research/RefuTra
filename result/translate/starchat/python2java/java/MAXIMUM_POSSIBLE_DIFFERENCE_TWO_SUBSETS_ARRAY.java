public static int f_gold ( int arr [ ], int n ) {
        int SubsetSum_1 = 0 ;
        int SubsetSum_2 = 0 ;
        for ( int i = 0 ; i < n ; i++ ) {
            boolean isSingleOccurance = true ;
            for ( int j = i + 1 ; j < n ; j++ ) {
                if ( arr [ i ] == arr [ j ] ) {
                    isSingleOccurance = false ;
                    arr [ i ] = arr [ j ] = 0 ;
                    break ;
                }
            }
            if ( isSingleOccurance == true ) {
                if ( arr [ i ] > 0 ) {
                    SubsetSum_1 += arr [ i ] ;
                } else {
                    SubsetSum_2 += arr [ i ] ;
                }
            }
        }
        return Math.abs ( SubsetSum_1 - SubsetSum_2 ) ;
    }