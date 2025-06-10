public static int f_gold ( int arr [ ], int n, int sum ) {
    int curr_sum = arr [ 0 ];
    int start = 0;
    for ( int i = 1 ; i <= n ; i++ ) {
        while ( curr_sum > sum && start < i - 1 ) {
            curr_sum = curr_sum - arr [ start ];
            start++;
        }
        if ( curr_sum == sum ) {
            System.out.println ( "Sum found between indexes" );
            System.out.println ( start + " and " + ( i - 1 ) );
            return 1;
        }
        if ( i < n ) {
            curr_sum = curr_sum + arr [ i ];
        }
    }
    System.out.println ( "No subarray found" );
    return 0;
}