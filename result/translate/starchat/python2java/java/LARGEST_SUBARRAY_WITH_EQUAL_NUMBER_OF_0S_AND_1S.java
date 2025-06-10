public static int f_gold ( int arr [ ] arr, int n ) {
        int sum = 0, max_size = -1, start_index = 0;
        for ( int i = 0; i < n - 1; i++ ) {
            sum = ( arr [ i ] == 0 )? -1 : 1;
            for ( int j = i + 1; j < n; j++ ) {
                sum = sum + ( arr [ j ] == 0 )? -1 : sum + 1;
                if ( sum == 0 && max_size < j - i + 1 ) {
                    max_size = j - i + 1;
                    start_index = i;
                }
            }
        }
        if ( max_size == -1 ) {
            System.out.println ( "No such subarray" );
        } else {
            System.out.println ( start_index + " to " + ( start_index + max_size - 1 ) );
        }
        return max_size;
    }