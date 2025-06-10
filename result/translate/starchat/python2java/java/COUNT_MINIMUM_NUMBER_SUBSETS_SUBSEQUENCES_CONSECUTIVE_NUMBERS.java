public static int f_gold ( int arr [ ] arr_size ) {
        Arrays.sort ( arr );
        int count = 1;
        for ( int i = 0 ; i < arr_size - 1 ; i++ ) {
            if ( arr [ i ] + 1!= arr [ i + 1 ] ) {
                count = count + 1;
            }
        }
        return count;
    }