public static int f_gold ( int arr [ ], int n, int k ) {
    int um [ ] = new int [ k ];
    int mod_arr [ ] = new int [ n ];
    int max = 0;
    int curr_sum = 0;
    for ( int i = 0 ; i < n ; i ++ ) {
        curr_sum += arr [ i ];
        mod_arr [ i ] = ( ( curr_sum % k ) + k ) % k;
    }
    for ( int i = 0 ; i < n ; i ++ ) {
        if ( mod_arr [ i ] == 0 ) {
            max = i + 1;
        } else if ( mod_arr [ i ] in um ) {
            um [ mod_arr [ i ] ] = i;
        } else {
            if ( max < ( i - um [ mod_arr [ i ] ] ) ) {
                max = i - um [ mod_arr [ i ] ];
            }
        }
    }
    return max;
    }