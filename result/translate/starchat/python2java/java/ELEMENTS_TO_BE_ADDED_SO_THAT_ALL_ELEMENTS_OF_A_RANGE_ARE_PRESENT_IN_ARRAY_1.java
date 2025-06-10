public static int f_gold ( int arr [ ], int n ) {
        HashMap < Integer, Integer > s = new HashMap < > ( );
        int count = 0, maxm = Integer. MIN_VALUE, minm = Integer. MAX_VALUE;
        for ( int i = 0; i < n; i++ ) {
            s.put ( arr [ i ], 1 );
            if ( arr [ i ] < minm ) minm = arr [ i ];
            if ( arr [ i ] > maxm ) maxm = arr [ i ];
        }
        for ( int i = minm; i <= maxm; i++ ) if (!s.containsKey ( i ) ) count++;
        return count;
    }