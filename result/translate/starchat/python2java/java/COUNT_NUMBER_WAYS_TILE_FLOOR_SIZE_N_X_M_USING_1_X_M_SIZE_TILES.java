public static int f_gold ( int n, int m ) {
        int[] count = new int[n + 2];
        for ( int i = 0; i < count.length; i++ ) {
            count[i] = 0;
        }
        count[0] = 0;
        for ( int i = 1; i <= n; i++ ) {
            if ( i > m ) {
                count[i] = count[i - 1] + count[i - m];
            } else if ( i < m ) {
                count[i] = 1;
            } else {
                count[i] = 2;
            }
        }
        return count[n];
    }