public static int f_gold ( int arr [ ], int n ) {
        Map < Integer, Integer > mp = new HashMap < > ( );
        int maxDict = 0;
        for ( int i = 0; i < n; i++ ) {
            if (!mp.containsKey ( arr [ i ] ) ) {
                mp.put ( arr [ i ], i );
            } else {
                maxDict = Math.max ( maxDict, i - mp.get ( arr [ i ] ) );
            }
        }
        return maxDict;
    }