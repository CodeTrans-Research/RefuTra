public static int f_gold ( int[] a, int size ) {
        int max_so_far = -1 * Integer.MAX_VALUE - 1;
        int max_ending_here = 0;
        int start = 0;
        int end = 0;
        for ( int i = 0; i < size; i++ ) {
            max_ending_here += a[i];
            if ( max_so_far < max_ending_here ) {
                max_so_far = max_ending_here;
                start = i;
                end = i;
            }
            if ( max_ending_here < 0 ) {
                max_ending_here = 0;
            }
        }
        return end - start + 1;
    }