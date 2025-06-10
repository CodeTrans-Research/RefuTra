public static int f_gold ( int start, int end, int arr [ ] ) {
        HashMap < Integer, Integer > frequency = new HashMap < > ( );
        for ( int i = start ; i <= end ; i ++ ) {
            if ( frequency.containsKey ( arr [ i ] ) ) {
                frequency.put ( arr [ i ], frequency.get ( arr [ i ] ) + 1 );
            } else {
                frequency.put ( arr [ i ], 1 );
            }
        }
        int count = 0;
        for ( int x : frequency.keySet ( ) ) {
            if ( frequency.get ( x ) == frequency.get ( x ).intValue ( ) ) {
                count += 1;
            }
        }
        return count;
    }