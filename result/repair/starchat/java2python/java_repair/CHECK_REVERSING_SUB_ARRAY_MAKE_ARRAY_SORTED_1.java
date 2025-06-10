  boolean f_gold ( int arr [ ], int n ) {
        if ( n == 1 ) {
            return true;
        }
        int i = 1;
        for ( i = 1 ; i < n ; i++ ) {
            if ( arr [ i - 1 ] >= arr [ i ] ) {
                break;
            } else {
                if ( i == n ) {
                    return true;
                }
            }
        }
        int j = i;
        i++;
        while ( arr [ j ] < arr [ j - 1 ] ) {
            if ( i > 1 && arr [ j ] < arr [ i - 2 ] ) {
                return false;
            }
            j++;
        }
        if ( j == n ) {
            return true;
        }
        int k = j;
        if ( arr [ k ] < arr [ i - 1 ] ) {
            return false;
        }
        while ( k > 1 && k < n ) {
            if ( arr [ k ] < arr [ k - 1 ] ) {
                return false;
            }
            k++;
        }
        return true;
    }
