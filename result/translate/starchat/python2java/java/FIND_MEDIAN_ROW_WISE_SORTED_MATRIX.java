public static int f_gold ( int[][] m, int r, int c ) {
        int mi = Integer.MAX_VALUE, mx = Integer.MIN_VALUE;
        for ( int i = 0; i < r; i++ ) {
            if ( m[i][0] < mi ) mi = m[i][0];
            if ( m[i][c-1] > mx ) mx = m[i][c-1];
        }
        int desired = (r*c+1) / 2;
        while ( mi < mx ) {
            int mid = mi + (mx-mi) / 2;
            int place = 0;
            for ( int i = 0; i < r; i++ ) {
                int j = Arrays.binarySearch(m[i], mid);
                place += j;
            }
            if ( place < desired ) mi = mid + 1;
            else mx = mid;
        }
        System.out.println("Median is " + mi);
        return mi;
    }