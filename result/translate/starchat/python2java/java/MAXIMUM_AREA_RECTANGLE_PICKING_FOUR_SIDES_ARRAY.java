public static int f_gold ( int arr [ ], int n ) {
    Arrays.sort ( arr ) ;
    int dimension [ ] = { 0, 0 } ;
    int i = 0, j = 0 ;
    while ( i < n - 1 && j < 2 ) {
        if ( arr [ i ] == arr [ i + 1 ] ) {
            dimension [ j ] = arr [ i ] ;
            j++ ;
            i++ ;
        }
        else i++ ;
    }
    return ( dimension [ 0 ] * dimension [ 1 ] ) ;
}