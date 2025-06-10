public static boolean f_gold ( int[] pre, int n ) {
        Stack < Integer > s = new Stack < > ( );
        int root = Integer.MIN_VALUE;
        for ( int i = 0; i < n; i++ ) {
            if ( pre [ i ] < root ) return false;
            while (!s.isEmpty() && s.peek() < pre [ i ] ) root = s.pop( );
            s.push(pre [ i ]);
        }
        return true;
    }