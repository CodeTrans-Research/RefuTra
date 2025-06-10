public static int f_gold ( int arr [ ] arr, int n, int k ) {
        PriorityQueue < Integer > pq = new PriorityQueue < > ( );
        for ( int i = 0 ; i < n ; i ++ ) {
            pq. add ( arr [ i ] );
        }
        int count = 0, ans = 1;
        while ( pq. size ( ) > 0 && count < k ) {
            ans += pq. poll ( );
            count ++;
        }
        return ans;
    }