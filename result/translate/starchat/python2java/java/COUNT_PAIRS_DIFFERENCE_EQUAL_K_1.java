public static int f_gold ( int arr [ ], int n, int k ) {
    Arrays.sort ( arr ) ;
    int count = 0, l = 0, r = 0 ;
    while ( r < n ) {
        if ( arr [ r ] - arr [ l ] == k ) {
            count++ ;
            l++ ;
            r++ ;
        }
        else if ( arr [ r ] - arr [ l ] > k ) {
            l++ ;
        }
        else {
            r++ ;
        }
    }
    return count ;
}