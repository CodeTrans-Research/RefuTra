public static int f_gold ( int arr [ ], int n ) {
        Deque < Integer > q = new ArrayDeque < > ( );
        for ( int i = 0 ;
  i < n ;
  i ++ ) {
            while (!q.isEmpty ( ) && arr [ i ] >= 2 * q.peek ( ) ) {
                q.remove ( );
            }
            q.add ( arr [ i ] );
        }
        return q.size ( );
    }