public static int f_gold ( int arr1 [ ], int arr2 [ ], int m, int n, int x ) {
        Set < Integer > us = new HashSet < > ( );
        for ( int i = 0 ; i < m ; i ++ ) us.add ( arr1 [ i ] );
        int count = 0;
        for ( int j = 0 ; j < n ; j ++ ) if ( x - arr2 [ j ] in us ) count ++;
        return count;
    }